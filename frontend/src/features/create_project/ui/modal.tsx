import { Button, Dialog, DialogBody, DialogHeader, Flex, Label, Sheet, Text, TextArea, TextInput } from "@gravity-ui/uikit";
import { ReactElement, useContext, useState } from "react";
import { FileInput } from "../../../shared/ui/fileInput";
import { useMediaQuery } from "react-responsive";
import { ProjectCreate } from "../model/schema";
import { CreateProject, SearchUser } from "../api/api";
import { UserContext } from "../../../app/providers/user";
import { Role } from "../../../entities/user";
import { AddNotify } from "../../../shared/ui/notify/notify";

interface Props {
    is_open: boolean;
    close_hook: () => void;
}

export const CreateProjectModal = ({ is_open, close_hook }: Props): ReactElement => {

    const isTabletOrMobile = useMediaQuery({ query: '(max-width: 1224px)' })
    const {updateUser} = useContext(UserContext);
    
    const [title, setTitle] = useState('');
    const [theme, setTheme] = useState('');
    const [way, setWay] = useState('');
    const [desc, setDesc] = useState('');
    const [files, setFiles] = useState<File[]>([]);

    const [ml, setMl] = useState('');
    const [ed, setEd] = useState('');
    const [edH, setEdH] = useState('');

    const [mlID, setMlID] = useState(0)
    const [edID, setEDID] = useState(0)
    const [edHID, setEDHID] = useState(0)

    const OnProjectCreate = () => {
        let data: ProjectCreate = {
            name: title,
            theme: theme,
            goal: way,
            target_desc: desc,
            users: JSON.stringify([ml, ed, edH])
        };
    
        const formData = new FormData();
        files.forEach(file => {
            formData.append('files', file);
        });
    
        // Создаем массив промисов для проверки пользователей
        const validationPromises = [
            SearchUser({ name: ml, role: Role.ANALYST }).then(users => {
                setMlID(users[0].id);
                return users.length > 0;
            }),
            SearchUser({ name: ed, role: Role.WRITER }).then(users => {
                setEDID(users[0].id);
                return users.length > 0;
            }),
            SearchUser({ name: edH, role: Role.HEAD_WRITER }).then(users => {
                setEDHID(users[0].id);
                return users.length > 0;
            })
        ];
    
        // Используем Promise.all для ожидания завершения всех проверок
        Promise.all(validationPromises)
            .then(results => {
                const [isMl, isEd, isEdH] = results; // Получаем результаты проверок
                data = {
                    name: title,
                    theme: theme,
                    goal: way,
                    target_desc: desc,
                    users: JSON.stringify([mlID, edID, edHID])
                };
                if (isMl && isEd && isEdH) {
                    return CreateProject(data, formData);
                } else {
                    throw new Error('Некоторые пользователи не подходят для своих ролей');
                }
            })
            .then(() => {
                updateUser();
                close_hook();
                AddNotify({
                    title: 'Успешно',
                    content: 'Ваш проект рассылки создан'
                });
            })
            .catch(()=> {
                AddNotify({
                    title: 'Ошибка',
                    content: 'Некоторые пользователи не подходят для своих ролей',
                    type: 'danger'
                });
            });
    };

    // Функция для удаления файла по индексу
    const removeFile = (index: number) => {
        setFiles(prevFiles => prevFiles.filter((_, i) => i !== index));
    };
    if (!isTabletOrMobile) {
    return (
        <Dialog size="m" onClose={close_hook} open={is_open}>
            <DialogHeader caption='Создание проекта'></DialogHeader>
            <DialogBody>
                    <Flex width={'100%'} gap={3} direction={'column'}>
                    <Text variant="header-1">Информация</Text>
                        <TextInput size="l" placeholder="Название проекта" value={title} onChange={(e) => setTitle(e.target.value)} />
                        <TextInput size="l" placeholder="Тема проекта" value={theme} onChange={(e) => setTheme(e.target.value)} />
                        <TextInput size="l" placeholder="Цель проекта" value={way} onChange={(e) => setWay(e.target.value)} />
                        <TextArea size="l" placeholder="Описание целевой аудитории проекта" value={desc} minRows={4} maxRows={6} onChange={(e) => setDesc(e.target.value)} />
                        <FileInput hook_func={setFiles} value={files} />
                            <Flex width={'100%'} maxWidth="s" gap={2} style={{ flexWrap: 'wrap' }}>
                                {files.map((file, index) => (
                                    <Label 
                                        key={file.name}
                                        type="close" 
                                        onCloseClick={() => removeFile(index)} 
                                        theme={"warning"}
                                    >
                                        {file.name}
                                    </Label>
                                ))}
                            </Flex>
                        <Text variant="header-1">Должности</Text>
                        <TextInput label="Аналитик:" size="m" value={ml} onChange={(e) => setMl(e.target.value)} />
                        <TextInput label="Редактор:" size="m" value={ed} onChange={(e) => setEd(e.target.value)} />
                        <TextInput label="Гл. редактор:" size="m" value={edH} onChange={(e) => setEdH(e.target.value)} />        
                    </Flex>
                </DialogBody>
                <Dialog.Footer
                onClickButtonCancel={close_hook}
                onClickButtonApply={OnProjectCreate}
                textButtonApply="Создать"
                />
        </Dialog>
    );
    } else {
        return <Sheet title="Создание проекта" onClose={close_hook} visible={is_open}>
        <Flex style={{padding: '8px'}}>
                <Flex width={'100%'} gap={3} direction={'column'}>
                    <TextInput size="l" placeholder="Название проекта" value={title} onChange={(e) => setTitle(e.target.value)} />
                    <TextInput size="l" placeholder="Тема проекта" value={theme} onChange={(e) => setTheme(e.target.value)} />
                    <TextInput size="l" placeholder="Цель проекта" value={way} onChange={(e) => setWay(e.target.value)} />
                    <TextArea size="l" placeholder="Описание целевой аудитории проекта" value={desc} minRows={4} maxRows={6} onChange={(e) => setDesc(e.target.value)} />
                    <FileInput hook_func={setFiles} value={files} />
                        <Flex width={'100%'} maxWidth="s" gap={2} style={{ flexWrap: 'wrap' }}>
                            {files.map((file, index) => (
                                <Label 
                                    key={file.name}
                                    type="close" 
                                    onCloseClick={() => removeFile(index)} 
                                    theme={"warning"}
                                >
                                    {file.name}
                                </Label>
                            ))}
                        </Flex>
                    <Text variant="header-1">Роли</Text>
                    <TextInput label="Аналитик:" size="m" value={ml} onChange={(e) => setMl(e.target.value)} />
                    <TextInput label="Редактор:" size="m" value={ed} onChange={(e) => setEd(e.target.value)} />
                    <TextInput label="Гл. редактор:" size="m" value={edH} onChange={(e) => setEdH(e.target.value)} />        
                </Flex>
            </Flex>
            <Flex gap={2} direction={'column'} style={{paddingBottom: '12px'}} spacing={{mt: 4}}>
                <Button size="l" width="max" view="action" onClick={OnProjectCreate}>Создать</Button>
                <Button size="l" width="max" view="normal" onClick={close_hook}>Закрыть</Button>
            </Flex>
    </Sheet>
    }
}
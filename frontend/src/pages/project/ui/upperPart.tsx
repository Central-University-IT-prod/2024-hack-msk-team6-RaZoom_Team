import { Flex, Text, Card, Label, Icon } from "@gravity-ui/uikit";
import styles from './style.module.scss';
import { ArrowDownToSquare } from '@gravity-ui/icons';
import { FileInfo } from "../../../entities/project";

interface Props {
    title: string;
    goal: string;
    descriptionTA: string;
    files: FileInfo[];
}

const UpperPart = ({ title, goal, descriptionTA, files }: Props) => {

    const onDownload = (url: string) => {
        window.open(url, "_blank", "noopener,noreferrer");
    };

    return (
        <Flex gap={6} direction={'column'} alignItems={'center'} justifyContent={'center'}>
            <Text className={styles['title']} variant="display-2">{title}</Text>
            <Card className={styles['card-container']} width={"75%"} view="outlined">
                <Flex gap={2} direction="column" alignItems="center" justifyContent="center" style={{ height: '100%' }}>
                    <Text variant="header-2">Цель:</Text>
                    <Text variant="body-3">{goal}</Text>
                </Flex>
            </Card>
            <Card className={styles['card-container']} view="outlined" width={"75%"}>
                <Flex gap={2} direction="column" alignItems="center" justifyContent="flex-start" style={{ height: '100%' }}>
                    <Text variant="header-2">Описание целевой аудитории:</Text>
                    <Text variant="body-3">{descriptionTA}</Text>
                </Flex>
            </Card>
            <Flex alignItems={'center'} width={"75%"} justifyContent={'flex-start'}>
                <Label theme="normal" size="m">
                    Файлы:
                </Label>
                <Flex gap={2} style={{ flexWrap: 'wrap', marginLeft: '10px' }}>
                    {files.map((file, index) => (
                        <Label
                            interactive
                            icon={<Icon data={ArrowDownToSquare} size={16} />}
                            key={index}
                            size="m"
                            type="default"
                            onClick={() => onDownload(file.url)}
                            theme={"warning"}
                        >
                            {file.filename}
                        </Label>
                    ))}
                </Flex>
            </Flex>
        </Flex>
    );
};

export default UpperPart;
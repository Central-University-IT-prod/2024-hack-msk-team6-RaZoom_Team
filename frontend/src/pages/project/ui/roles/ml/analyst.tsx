import { Flex, Text, Card, Label, RadioButton, RadioButtonOption, Button } from "@gravity-ui/uikit";
import styles from '../../style.module.scss';
import { useState } from "react";

const AnalystLowerPart = () => {
    const genders: RadioButtonOption[] = [
        { value: 'female', content: 'Женский' },
        { value: 'male', content: 'Мужской' },
        { value: 'all', content: 'Не выбрано' }, 
    ];

    const ages: RadioButtonOption[] = [
        { value: 'child', content: 'Дети' },
        { value: 'teenager', content: 'Подростки' },
        { value: 'adult', content: 'Взрослые' },
        { value: 'pensioner', content: 'Пожилые' },
        { value: 'all', content: 'Не выбрано' }, 
    ];

    const statuses: RadioButtonOption[] = [
        { value: 'new', content: 'Новичок' },
        { value: 'regular', content: 'Постоянный' },
        { value: 'uninterested', content: 'Спящий' },
        { value: 'all', content: 'Не выбрано' }, 
    ];

    // Везде не выбрано
    const [selectedGender, setGender] = useState<string>('all'); 
    const [selectedAge, setAge] = useState<string>('all'); 
    const [selectedStatus, setStatus] = useState<string>('all'); 

    // Функция обработки нажатия кнопки
    const handleSubmit = () => {
        console.log('Выбранные значения:', {
            gender: selectedGender,
            age: selectedAge,
            status: selectedStatus,
        });
    };
    return (
        <Flex direction={'column'} alignItems={'center'} justifyContent={'center'} width={'100%'} height={'100%'} gap={10}>
            <Card className={styles['card-container']} width={"75%"} view="outlined">
                <Flex direction={'column'} alignItems={'stretch'} gap={5}>
                <Text variant="header-2">Настройка целевой аудитори</Text>
                    <Flex justifyContent="space-between" alignItems="center">
                        <Label theme="clear" size="m">Пол:</Label>
                        <RadioButton
                            value={selectedGender}
                            options={genders}
                            name="genderGroup"
                            onUpdate={setGender}
                            size="l"
                            width="auto"
                        />
                    </Flex>
                    <Flex justifyContent="space-between" alignItems="center">
                        <Label theme="clear" size="m">Возраст:</Label>
                        <RadioButton
                            value={selectedAge}
                            options={ages}
                            name="ageGroup"
                            onUpdate={setAge}
                            size="l"
                            width="auto"
                        />
                    </Flex>
                    <Flex justifyContent="space-between" alignItems="center">
                        <Label theme="clear" size="m">Статус клиента:</Label>
                        <RadioButton
                            value={selectedStatus}
                            options={statuses}
                            name="statusGroup"
                            onUpdate={setStatus}
                            size="l"
                            width="auto"
                        />
                    </Flex>
                </Flex>
            </Card>
            <Flex>
                <Button view="action" type='button' size="l" onClick={handleSubmit}>
                    Отправить
                </Button>
            </Flex>
        </Flex>
    );
};

export default AnalystLowerPart;
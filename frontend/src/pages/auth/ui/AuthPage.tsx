import { Flex, TextInput, Button, RadioButton, RadioButtonOption, Select } from '@gravity-ui/uikit';
import { useContext, useState } from 'react';
import React from 'react';
import { Login, Register } from '../api/api';
import Cookies from 'js-cookie';
import { UserLogin, UserRegister } from '../model/schema';
import { UserContext } from '../../../app/providers/user';

const AuthPage = () => {
    const [role, setRole] = useState<Role | null>(null);
    const [email, setEmail] = useState<string>('');
    const [name, setName] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const [values, setValues] = useState<string>('Регистрация');
    const [showErrors, setShowErrors] = useState<boolean>(false);

    const {updateUser} = useContext(UserContext)

    const options: RadioButtonOption[] = [
        { value: 'Регистрация', content: 'Регистрация' },
        { value: 'Вход', content: 'Вход' }
    ];

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        setShowErrors(true);

        let hasErrors = false;

        if (values === 'Регистрация') {
            if (!email || !name || !password || role === null) {
                hasErrors = true;
            }
            if (!hasErrors && role) {
                const registrationData: UserRegister = { email, name, password, role }; // Use main_role as per your schema
                Register(registrationData).then((response) => {
                    Cookies.set('Authorization', response);
                    updateUser()
                })
            }
        } else {
            if (!email || !password) {
                hasErrors = true;
            }
            if (!hasErrors) {
                const loginData: UserLogin = { email, password };
                Login(loginData).then((response) => {
                    Cookies.set('Authorization', response);
                    updateUser()
                })
                console.log('Login data:', loginData);
            }
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <Flex centerContent width={"100%"} height={"100%"} justifyContent={'center'} alignItems={'center'} minWidth={"40%"} minHeight={"40%"}>
                <Flex direction="column" centerContent justifyItems="center">
                    <Flex centerContent>
                        <RadioButton
                            defaultValue={options[0].value}
                            options={options}
                            name="authGroup"
                            onUpdate={setValues}
                            size="l"
                            width="auto" />
                    </Flex>
                    <Flex centerContent spacing={{ m: 5 }}>
                        <h1>{values === 'Регистрация' ? "Создайте аккаунт" : "Войдите в аккаунт"}</h1>
                    </Flex>
                    <Flex direction="column" space="5">
                        {values === 'Регистрация' && (
                            <Select size='l' label={'Роль:'} width={"max"} errorMessage={showErrors && role === null ? "Выберите роль" : undefined} onUpdate={(e) => { 
                                setRole(Number(e[0])); // Convert to number for enum
                            }}>
                                <Select.Option value={Role.PRODUCT.toString()}>Продакт</Select.Option>
                                <Select.Option value={Role.ANALYST.toString()}>Аналитик</Select.Option>
                                <Select.Option value={Role.WRITER.toString()}>Редактор</Select.Option>
                                <Select.Option value={Role.HEAD_WRITER.toString()}>Главный редактор</Select.Option>
                            </Select>
                        )}
                        <TextInput 
                            label="Почта:" 
                            validationState={showErrors && !email ? "invalid" : undefined} 
                            type="email" 
                            errorMessage={showErrors && !email ? "Введите почту" : undefined} 
                            value={email} 
                            onChange={(e) => setEmail(e.target.value)} 
                            size='l' 
                        />
                        {values === 'Регистрация' && (
                            <TextInput 
                                label="Имя:" 
                                validationState={showErrors && !name ? "invalid" : undefined} 
                                type="text" 
                                errorMessage={showErrors && !name ? "Введите имя" : undefined} 
                                value={name} 
                                onChange={(e) => setName(e.target.value)} 
                                size='l' 
                            />
                        )}
                        <TextInput 
                            label="Пароль:" 
                            validationState={showErrors && !password ? "invalid" : undefined} 
                            type="password" 
                            errorMessage={showErrors && !password ? "Введите пароль" : undefined} 
                            value={password} 
                            onChange={(e) => setPassword(e.target.value)} 
                            size='l' 
                        />
                        <Flex centerContent spacing={{ m: 1 }} width="auto">
                            <Button width='max' view="action" type='submit' size="l">
                                {values === 'Регистрация' ? "Создать" : "Войти"}
                            </Button>
                        </Flex>
                    </Flex>
                </Flex>
            </Flex>
        </form>
    );
};

export enum Role {
    PRODUCT = 0,
    WRITER = 1,
    HEAD_WRITER = 2,
    ANALYST = 3
}

export default AuthPage;
import { AxiosError } from "axios";
import { UserClient } from "../../../entities/user/api/client" 
import { AddErrorNotify } from "../../../shared/ui/notify/notifyError";
import { UserLogin, UserRegister } from '../model/schema';
import Cookies from "js-cookie";

export const Login = async (data: UserLogin): Promise<string> => {
    return UserClient.post('/auth', data)
    .then(response => {
        if (response.data) {
            return response.data.session
        }
        return response.data
    })
    .catch((error: AxiosError) => {
        console.log(error)
        //@ts-ignore
        AddErrorNotify(error!.response!.data!.code)
        Cookies.remove('Authorization')
        throw error
    }) 
}

export const Exit = async (): Promise<boolean> => {
    return UserClient.delete('/auth')
    .then(response => {
        if (response.data) {
            return response.data.session
        }
        return response.data
    })
    .catch((error: AxiosError) => {
        console.log(error)
        //@ts-ignore
        AddErrorNotify(error!.response!.data!.code)
        Cookies.remove('Authorization')
        throw error
    }) 
}

export const Register = async (data: UserRegister): Promise<string> => {
    return UserClient.post('/users', data)
    .then(response => {
        if (response.data) {
            return response.data.session
        }
        return response.data
    })
    .catch((error: AxiosError) => {
        console.log(error)
        //@ts-ignore
        AddErrorNotify(error!.response!.data!.code)
        Cookies.remove('Authorization')
        throw error
    }) 
}
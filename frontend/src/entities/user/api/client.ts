import axios from "axios";
import Cookies from 'js-cookie'
import { API_URL } from "../../../shared/config";

export const UserClient = axios.create({
    baseURL: API_URL,
})

UserClient.interceptors.request.use(config => {
    const authCookie = Cookies.get('Authorization')
    config.headers['Authorization'] = authCookie;
    return config
})
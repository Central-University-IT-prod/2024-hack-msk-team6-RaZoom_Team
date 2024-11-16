import { Role } from "../../../entities/user"

export interface UserRegister  {
    name: string
    email: string
    role: Role
    password: string
}

export interface UserLogin {
    email: string
    password: string
}
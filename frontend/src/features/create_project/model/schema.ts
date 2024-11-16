import { Role } from "../../../entities/user"

export interface ProjectCreate {
    name: string
    theme: string
    target_desc: string
    goal: string
    users: string
}

export interface SearchUserModel {
    name: string
    role: Role
}

export interface UserAfterSearch {
    id: number
    name: string
    email: string
    role: Role
}
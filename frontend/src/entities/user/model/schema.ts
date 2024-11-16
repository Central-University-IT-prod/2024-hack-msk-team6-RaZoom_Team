import { ProjectInfo } from "../../project"

export type User = {
    id: number,
    role: Role,
    name: string,
    email: string,
    working_projects: ProjectInfo[]
}

export enum Role {
    PRODUCT = 0,
    WRITER = 1,
    HEAD_WRITER = 2,
    ANALYST = 3
}
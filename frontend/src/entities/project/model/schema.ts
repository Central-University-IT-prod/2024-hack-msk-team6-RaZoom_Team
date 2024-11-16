import { AproveAnswer, EditorAnswer, MlAnswer } from "../../../pages/project/modal/schema"
import { Role } from "../../user"

export type ProjectInfo = {
    id: number,
    name: string,
    theme: string,
    targes_desc: string,
    goal: string
}

export type Project = {
    id: number,
    name: string,
    theme: string,
    targes_desc: string,
    goal: string,
    users: ProjectUser[],
    attachements: FileInfo[],
    stages: Stage[]
}

export type FileInfo = {
    filename: string,
    url: string
}

interface ProjectUser {
    id: number,
    name: string,
    role: Role
}

export type Payload = MlAnswer | AproveAnswer | EditorAnswer // То что отправляется в одной из стадий

export type Stage = {
    id: number,
    stage: StageType,
    status: Status,
    payload?: Payload,
    comment?: string,
    history?: Payload[] // История отправок из разных стадий
}

export enum StageType {
    WRITE_TEXT = 0,
    APPROVE_TEXT = 1,
    ANALYSIS = 2,
    APPROVE = 3
}

export enum Status {
    WAITING = 0,
    WORKING = 1,
    COMPLETED = 2
}

interface StateRight {
    executor: Role,
    access: Role[]
}

export const StageRights: Record<StageType, StateRight> = {
    [StageType.WRITE_TEXT]: {
        executor: Role.WRITER,
        access: [Role.HEAD_WRITER]
    },
    [StageType.APPROVE_TEXT]: {
        executor: Role.HEAD_WRITER,
        access: []
    },
    [StageType.ANALYSIS]: {
        executor: Role.ANALYST,
        access: []
    },
    [StageType.APPROVE]: {
        executor: Role.HEAD_WRITER,
        access: []
    },
}
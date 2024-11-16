import { AddErrorNotify } from "../../../shared/ui/notify/notifyError"
import { UserClient } from "../../user/api/client"
import { Project } from "../model/schema"

export const getProject = async(id: string): Promise<Project> => {
    return UserClient.post('/project/'+id)
    .then(response => {
        return response.data
    })
    .catch((error) => {
        if (error) AddErrorNotify(error.status)
        console.log(error)
        throw error
    })
}


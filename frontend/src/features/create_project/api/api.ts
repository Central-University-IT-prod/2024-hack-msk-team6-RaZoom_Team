import { AxiosError } from "axios";
import { UserClient } from "../../../entities/user/api/client"
import { ProjectCreate, SearchUserModel, UserAfterSearch,  } from "../model/schema"
import { AddErrorNotify } from "../../../shared/ui/notify/notifyError";

export const CreateProject = async(data: ProjectCreate, files: FormData) => {
    return UserClient.post('/projects', files, {params: data})
    .then(response => {
        return response.data;
    })
    .catch((error: AxiosError) => {
        console.log(error);
        if (error.status) AddErrorNotify(error.status)
        throw error;
    })
}

export const SearchUser = async(data: SearchUserModel): Promise<UserAfterSearch[]> => {
    return UserClient.post('/users/search', data)
    .then(response => {
        return response.data;
    })
    .catch((error: AxiosError)  => {
        console.log(error);
        if (error.status) AddErrorNotify(error.status)
        throw error
    })
}
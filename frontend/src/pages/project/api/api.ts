import { UserClient } from "../../../entities/user/api/client" 

export const getFiles = async (fileId: string) : Promise<string> => {
    return UserClient.get('/attachements', {params: { fileId: fileId }})
    .then(response => {
        return response.data
    })
    .catch(error => {
        console.log(error)
        throw error
    }
    ) 
}
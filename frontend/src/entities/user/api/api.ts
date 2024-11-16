import { User } from "../model/schema"
import { UserClient } from "./client"

export const getUser = async (): Promise<User> => {
    return UserClient.get('/users')
    .then(response => {
        return response.data
    })
    .catch(error => {
        console.log(error)
        throw error
    }
    ) 
}
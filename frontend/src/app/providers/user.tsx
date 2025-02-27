import { createContext, Dispatch, ReactNode, SetStateAction, useEffect, useState } from "react";
import { getUser, User } from "../../entities/user";
import { Loader } from "@gravity-ui/uikit";

interface IChildren {
    children: ReactNode;
}

interface Props {
    user: User | undefined | null;
    updateUser: () => void;
    setUser: Dispatch<SetStateAction<User | null | undefined>>;
}

export const UserContext = createContext<Props>({} as Props);

export default function UserProvider({ children }: IChildren) {

    const [user, setUser] = useState<User | undefined | null>(undefined);

    const updateUser = () => {
        getUser().then(setUser).catch(() => {
            setUser(null);
        })
        //console.log(user)
    }

    useEffect(() => {
        updateUser();
    }, []);

    useEffect(() => {
        //console.log(user)
    }, [user])
    
    if (user === undefined) {
        return <Loader size="l"></Loader>
    }
    return (
        <UserContext.Provider value={{ user, updateUser, setUser }}>
            {children}
        </UserContext.Provider>
    );
}
import { DropdownMenu, Flex, User } from "@gravity-ui/uikit"
import { useContext } from "react"
import { UserContext } from "../../../app/providers/user"
import { ThemeButton } from "../themeButton"
import { useMediaQuery } from "react-responsive"
import { Exit } from "../../../pages/auth/api/api"
import Cookies from "js-cookie"

interface Props {
    theme: 'dark' | 'light'
    setTheme: (value: 'dark' | 'light') => void
}

export const Header = ({setTheme, theme}: Props) => {
    const {user, updateUser} = useContext(UserContext)
    const isTabletOrMobile = useMediaQuery({ query: '(max-width: 1224px)' })

    const onExit = () => {
        Exit().then(() => {
            Cookies.remove('Authorization')
            updateUser()
        })
    }

    return <Flex spacing={{mt: 6, mb: 8}} height={'76px'} alignItems={"center"} width='100%' justifyContent={"space-around"}>
         <Flex gap={3} alignItems={'center'}>
{  user ?<DropdownMenu
                    items={[
                        {
                            action: onExit,
                            text: 'Выйти',
                        }
                    ]}/> : null}
            {
            user ?  
                <User size="l" avatar={{text: user.name, theme: 'brand'}} name={isTabletOrMobile ? '' : user.name} description={isTabletOrMobile ? '' : user.email}></User>
            :
                null
            }
            </Flex>
            <ThemeButton value={theme} setValue={setTheme}></ThemeButton>
        </Flex> 
}
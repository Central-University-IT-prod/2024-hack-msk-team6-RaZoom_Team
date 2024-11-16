import { useContext, useState } from "react"
import { UserContext } from "../../../app/providers/user"
import { Button, Flex, Icon, Text } from "@gravity-ui/uikit"
import {Plus} from '@gravity-ui/icons';
import styles from './style.module.scss'
import { WidgetProjectList } from "../../../widgets/projects/ui/projects";
import { CreateProjectModal } from "../../../features/create_project/ui/modal";

export const HomePage = () => {
    const {user} = useContext(UserContext)
    
    const [modal, setModal] = useState(false)
    if (user)
    return <Flex direction={'column'}  alignItems={'center'} justifyContent={'center'} width={'100%'}>
        <CreateProjectModal close_hook={() => setModal(false)} is_open={modal}/>
        <Flex spacing={{mt: 2}} alignItems={'center'} direction={'column'} justifyContent={'center'} width={'70%'}>
            <Text className={styles['title']} variant="display-2">Мои проекты</Text>
            <Flex spacing={{mt: 4}} gap={5}> 
                <Button onClick={() => setModal(true)} size="l" view="action">Создать <Icon data={Plus}></Icon></Button>
            </Flex>
        </Flex>
        <Flex spacing={{mt: 2}}>
            <WidgetProjectList projects={user.working_projects}></WidgetProjectList>
        </Flex>
    </Flex>
}
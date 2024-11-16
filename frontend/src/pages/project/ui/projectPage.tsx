import { Flex, Loader } from "@gravity-ui/uikit"
import { getProject, Project } from "../../../entities/project"
import UpperPart from "./upperPart"
import { LowerPart } from "./lowerPart"
import { useContext, useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import { UserContext } from "../../../app/providers/user"
import { AxiosError } from "axios"
import { AddErrorNotify } from "../../../shared/ui/notify/notifyError"

export const ProjectPage = () => {
    const {user} = useContext(UserContext)
    const { id } = useParams<{ id: string }>(); // Извлекаем id из параметров маршрута
    const [projectData, setProject] = useState<undefined | Project>(undefined);

    useEffect(() => {
        if (id) { // Проверяем, что id существует
            getProject(id)
                .then(setProject)
                .catch((error: AxiosError) => {
                    if(error.status) AddErrorNotify(error.status)
                    console.error('Ошибка при загрузке проекта:', error);
                });
        }
    }, []);

    if (projectData && user) {
    return <Flex direction={'column'}>
        <UpperPart title={projectData.name} goal={projectData.goal} descriptionTA={projectData.targes_desc} files={projectData.attachements}></UpperPart>
        <LowerPart role={user.role} stages={projectData.stages}/>
    </Flex> 
    } else return <Loader size="l"/>
}
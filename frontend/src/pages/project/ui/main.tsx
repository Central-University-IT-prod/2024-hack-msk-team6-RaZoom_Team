import { Flex } from "@gravity-ui/uikit";
import { Project } from "../../../entities/project";
import UpperPart from "./upperPart";
import { LowerPart } from "./lowerPart";
import { Role } from "../../../entities/user";

interface Props {
    project: Project;
    role: Role;
}

export const ProjectPage = ({ project, role }: Props) => {
    return (
        <Flex>
            <UpperPart 
                title={project.name} 
                goal={project.goal} 
                descriptionTA={project.targes_desc} 
                // @ts-ignore
                files={project.attachements} 
            />
            <LowerPart 
                role={role} 
                // @ts-ignore
                stages={project.stages} // Убедитесь, что stages определены в проекте
            />
        </Flex>
    );
};
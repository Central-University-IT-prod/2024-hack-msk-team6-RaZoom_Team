import { Stage, StageRights } from "../../../entities/project"
import { Role } from "../../../entities/user"
import EditorLowerPart from "./roles/editor/editor"
import { HeaderEditorLowerPart } from "./roles/editor/headEditor"
import AnalystLowerPart from "./roles/ml/analyst"
import { ProductLowerPart } from "./roles/product/product"

interface Props {
    role: Role
    stages: Stage[]
}


export const LowerPart = ({role, stages}: Props) => {
    stages = stages.filter(
        x => role in StageRights[x.stage].access || role == Role.PRODUCT || role == StageRights[x.stage].executor
    )
    switch (role) {
        case Role.ANALYST:
            return <AnalystLowerPart/>
        case Role.WRITER:
            // @ts-ignore
            return <EditorLowerPart/>
        case Role.HEAD_WRITER:
            return <HeaderEditorLowerPart/>
        case Role.PRODUCT:
            return <ProductLowerPart/>
        default:
            return <></>
    }
}
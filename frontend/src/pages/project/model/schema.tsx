import { FileInfo, Stage } from "../../../entities/project";

export type UpperPartProps = {
  title: string;
  goal: string
  descriptionTA: string
  files: FileInfo[];
}

export interface EditorAnswer {
  text: string
}

export interface MlAnswer {
  gender: 'male' | 'female' | 'all'
  age: "child" | "teenager" | "adult" | "pensioner" | "all"
  status: "new" | "main" | "sleeping" | "all"
}

export interface AproveAnswer {
  stage: Stage
  comment: string
}

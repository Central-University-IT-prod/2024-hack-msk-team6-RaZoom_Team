import { useFileInput, Button, Icon } from "@gravity-ui/uikit";
import React from "react";
import { FileArrowUp } from '@gravity-ui/icons';

interface Props {
    value: File[];
    hook_func: React.Dispatch<React.SetStateAction<File[]>>;
}

export const FileInput = ({ hook_func, value }: Props) => {
    const onUpdate = React.useCallback((files: File[]) => {
        // Создаем новый массив с добавленным файлом
        const newValue = [...value, ...files]; // Добавляем все загруженные файлы
        hook_func(newValue); 
    }, [hook_func, value]);

    const {
      controlProps,
      triggerProps
    } = useFileInput({
      onUpdate
    });

    return (
        <React.Fragment>
            <input {...controlProps} />
            <Button  width="auto" size="m" view="outlined" {...triggerProps}>
                Загрузить<Icon data={FileArrowUp} />
            </Button>
        </React.Fragment>
    );
}
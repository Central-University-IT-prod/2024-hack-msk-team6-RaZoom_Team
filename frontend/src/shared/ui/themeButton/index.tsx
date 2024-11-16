import { Icon, RadioButton, RadioButtonOption } from "@gravity-ui/uikit";
import { Sun, Moon } from '@gravity-ui/icons';

interface Props {
    value: 'dark' | 'light';
    setValue: (value: 'dark' | 'light') => void;
}

export const ThemeButton = ({ value, setValue }: Props) => {
    const options: RadioButtonOption[] = [
        {
            content: <Icon data={Moon}/>,
            value: "dark",
        },
        {
            content: <Icon data={Sun}/>,
            value: "light",
        }
    ];

    return (
        <RadioButton
        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        //@ts-expect-error
            options={options}
            value={value}
            onUpdate={setValue} 
        >
        </RadioButton>
    );
}
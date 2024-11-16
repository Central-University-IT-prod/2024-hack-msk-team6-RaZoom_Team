import { Button, Flex, Text } from "@gravity-ui/uikit"
import ReactDOMClient from 'react-dom/client';
import {Toaster} from '@gravity-ui/uikit';
import { isMobile } from "react-device-detect";

Toaster.injectReactDOMClient(ReactDOMClient);
const toaster = new Toaster({mobile: isMobile});

interface Props {
    title: string
    content: string
    type?: "success" | "normal" | "info" | "warning" | "danger" | "utility" | undefined
}

export function AddNotify({title, content, type}: Props) {

    const contentToaster = <Flex gap={2} direction={'column'}>
        <Text variant="body-1">{content}</Text>
        <Button size='l' onClick={() => toaster.remove(title)}>Понятно</Button>
    </Flex>

    toaster.add({
        title: title,
        name: title,
        content: contentToaster,
        theme: (type ? type : 'success')
    })
}
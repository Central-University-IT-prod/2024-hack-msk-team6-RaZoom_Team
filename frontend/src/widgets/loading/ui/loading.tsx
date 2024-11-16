import { Flex, Loader } from "@gravity-ui/uikit"

export const Loading = () => {
    return <Flex height={'100vh'} width={'100%'} justifyContent={'center'} alignItems={'center'}>
        <Loader size="l"></Loader>
    </Flex>
}
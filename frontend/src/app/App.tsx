import AppRoutes from './routes/AppRoutes'
import {ThemeProvider} from '@gravity-ui/uikit'
import '@gravity-ui/uikit/styles/fonts.css';
import '@gravity-ui/uikit/styles/styles.css';
import { Header } from '../shared/ui/header';
import { useState } from 'react';
import UserProvider from './providers/user';

const App = () => {
  const [theme, setTheme] = useState<'dark' | 'light'>('dark')
  return (
    <ThemeProvider theme={theme}>
      <UserProvider>
        <Header setTheme={(e) => setTheme(e as 'dark' | 'light')} theme={theme}/> 
        <AppRoutes/>
      </UserProvider>
    </ThemeProvider>
  );
};

export default App

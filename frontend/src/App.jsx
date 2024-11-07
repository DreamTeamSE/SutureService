import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Navbar from './components/ui-components/Navbar';
import Links from './routes/Links';
import { BrowserRouter as Router } from 'react-router-dom';

const theme = createTheme({
  palette: {
    mode: 'light', // Change to 'dark' for dark mode
    primary: {
      main: '#7678ed', // Customize primary color
    },
    secondary: {
      main: '#dc004e', // Customize secondary color
    },
    background: {
      default: '#F2F8FF', // Background color for the app
    },
  },
});

// HIkfremfer


function App() {

  return (
    <>
    <Router>
     <ThemeProvider theme={theme}>
      <CssBaseline />
      <Navbar />
      <Links />
      </ThemeProvider>
    </Router>
    </>
  )
}

export default App

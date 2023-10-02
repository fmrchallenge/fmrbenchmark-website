import './globals.css';

export const metadata = {
    title: 'Benchmarks on Formal Methods for Robotics',
};

export default function RootLayout({ children }: { children: React.ReactNode })
{
    return (
        <html lang="en">
            <body>
                <main className="min-h-screen bg-background flex flex-col items-center">
                    {children}
                </main>
            </body>
        </html>
    );
}

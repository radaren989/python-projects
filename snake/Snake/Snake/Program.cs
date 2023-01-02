using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace Snake
{
    class Program
    {
        static char[,] board = new char[41,21];
        class Snake
        {
            public int x;
            public int y;
            public char head;
            public Snake(int x, int y)
            {
                this.x = x;
                this.y = y;
                this.head = '#';
            }

            public void Movement(ConsoleKeyInfo dir)
            {
                if (dir.KeyChar == 68 || dir.KeyChar == 100)
                {
                    board[x, y] = ' ';
                    this.x++;
                    board[x, y] = '#';

                }
                else if (dir.KeyChar == 83 || dir.KeyChar == 115)
                {
                    board[x, y] = ' ';
                    this.y++;
                    board[x, y] = '#';
                }
                else if (dir.KeyChar == 65 || dir.KeyChar == 97)
                {
                    board[x, y] = ' ';
                    this.x--;
                    board[x, y] = '#';
                }
                else if (dir.KeyChar == 87 || dir.KeyChar == 119)
                {
                    board[x, y] = ' ';
                    this.y--;
                    board[x, y] = '#';
                }    
            }
        }
        static void Main(string[] args)
        {
            ConsoleKeyInfo cki;
            Snake s = new Snake(1, 1);
            SetBoundries();
            while (true)
            {
                if (Console.KeyAvailable)
                {
                    cki = Console.ReadKey(true);
                    s.Movement(cki);
                }
                Screen();
                Thread.Sleep(1000);

            }

            Console.ReadKey();
        }

        static void Screen()
        {
            for (int x = 0; x < board.GetLength(0); x++)
            {
                for (int y = 0; y < board.GetLength(1); y++)
                {
                    Console.SetCursorPosition(x, y);
                    Console.Write(board[x,y]);
                }
            }
        }
        static void SetBoundries()
        {
            for (int x = 0; x < board.GetLength(0); x++)
            {
                for (int y = 0; y < board.GetLength(1); y++)
                {
                    if(x == 0 || y == 0 || x == 40 || y == 20)
                    {
                        board[x, y] = 'x';
                    }
                }
            }
        }
    }
}

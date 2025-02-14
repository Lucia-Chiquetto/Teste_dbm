using Microsoft.EntityFrameworkCore;
using Repositories;
using Repositories.Models;

namespace APITeste.Repositories
{
    public class PessoaRepository : IPessoaRepository
    {
        private readonly ApplicationDbContext _context;

        public PessoaRepository(ApplicationDbContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<Pessoa>> GetAllAsync()
        {
            return await _context.Pessoas.ToListAsync();
        }

        public async Task<Pessoa> GetByIdAsync(int id)
        {
            return await _context.Pessoas.FindAsync(id);
        }

        public async Task AddAsync(Pessoa pessoa)
        {
            await _context.Pessoas.AddAsync(pessoa);
            await _context.SaveChangesAsync();
        }

        public async Task AddRangeAsync(IEnumerable<Pessoa> pessoas)
        {
            await _context.Pessoas.AddRangeAsync(pessoas);
            await _context.SaveChangesAsync();
        }
    }
}

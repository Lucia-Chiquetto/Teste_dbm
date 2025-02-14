using Repositories.Models;

namespace APITeste.Repositories
{
    public interface IPessoaRepository
    {
        Task<IEnumerable<Pessoa>> GetAllAsync();
        Task<Pessoa> GetByIdAsync(int id);
        Task AddAsync(Pessoa pessoa);
        Task AddRangeAsync(IEnumerable<Pessoa> pessoas);
    }
}

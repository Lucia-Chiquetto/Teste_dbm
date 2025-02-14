using Repositories.Models;

namespace APITeste.Services
{
    public interface IPessoaService
    {
        Task<IEnumerable<Pessoa>> GetAllAsync();
        Task<Pessoa> GetByIdAsync(int id);
        Task AddAsync(Pessoa pessoa);
        Task AddRangeAsync(Stream arquivo);
    }
}

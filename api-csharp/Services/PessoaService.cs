using APITeste.Repositories;
using Repositories.Models;

namespace APITeste.Services
{
    public class PessoaService : IPessoaService
    {
        private readonly IPessoaRepository _pessoaRepository;

        public PessoaService(IPessoaRepository pessoaRepository)
        {
            _pessoaRepository = pessoaRepository;
        }

        public async Task<IEnumerable<Pessoa>> GetAllAsync()
        {
            return await _pessoaRepository.GetAllAsync();
        }

        public async Task<Pessoa> GetByIdAsync(int id)
        {
            return await _pessoaRepository.GetByIdAsync(id);
        }

        public async Task AddAsync(Pessoa pessoa)
        {
            await _pessoaRepository.AddAsync(pessoa);
        }

        public async Task AddRangeAsync(Stream arquivo)
        {
            var pessoas = new List<Pessoa>();

            using var reader = new StreamReader(arquivo);

            string? line;
            while ((line = await reader.ReadLineAsync()) != null)
            {
                var values = line.Split(',');

                if (values.Length < 4) continue;

                if (int.TryParse(values[1], out int idade))
                {
                    pessoas.Add(new Pessoa
                    {
                        Nome = values[0].Trim(),
                        Idade = idade,
                        Cidade = values[2].Trim(),
                        Profissao = values[3].Trim()
                    });
                }
            }

            if (pessoas.Count > 0)
            {
                await _pessoaRepository.AddRangeAsync(pessoas);
            }
        }

    }
}

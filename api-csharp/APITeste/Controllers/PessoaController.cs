using APITeste.Services;
using Microsoft.AspNetCore.Mvc;
using Repositories.Models;

namespace APITeste.Controllers;

[ApiController]
[Route("[controller]")]
public class PessoaController : ControllerBase
{
    private readonly ILogger<PessoaController> _logger;
    private readonly IPessoaService _pessoaService;
    
    public PessoaController(IPessoaService pessoaService)
    {
        _pessoaService = pessoaService;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<Pessoa>>> GetAll()
    {
        var pessoas = await _pessoaService.GetAllAsync();
        return Ok(pessoas);
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<Pessoa>> GetById(int id)
    {
        var pessoa = await _pessoaService.GetByIdAsync(id);
        if (pessoa == null)
            return NotFound($"Pessoa com ID {id} não encontrada.");

        return Ok(pessoa);
    }

    [HttpPost("importar-csv")]
    public async Task<ActionResult> ImportCsv()
    {
        try
        {
            var arquivo = Request.Body;

            if (arquivo == null)
                return BadRequest("Nenhum dado fornecido.");

            await _pessoaService.AddRangeAsync(arquivo);
            return Ok("Dados importados com sucesso.");
        }
        catch(Exception ex)
        {
            return BadRequest();
        }
    }
}

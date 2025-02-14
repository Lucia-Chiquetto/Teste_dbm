using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Repositories.Models;

namespace Repositories
{
    public class ApplicationDbContext : DbContext
    {
        public DbSet<Pessoa> Pessoas { get; set; }

        private readonly IConfiguration _configuration;

        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options, IConfiguration configuration)
            : base(options)
        {
            _configuration = configuration;
        }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseSqlServer(_configuration.GetConnectionString("DefaultConnection"));
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Pessoa>(entity =>
            {
                entity.HasKey(e => e.Id);
                entity.Property(e => e.Nome).IsRequired().HasMaxLength(100);
                entity.Property(e => e.Idade);
                entity.Property(e => e.Cidade);
                entity.Property(e => e.Profissao);
            });

            base.OnModelCreating(modelBuilder);
        }
    }
}

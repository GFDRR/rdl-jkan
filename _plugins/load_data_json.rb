module Jekyll
  module LoadDataJsonFilter
    def load_data_json(dir)
      json_dir = File.join(Jekyll.sites.first.source, dir)
      merged_datasets = []
      
      Dir.glob(File.join(json_dir, '*.json')).sort.each do |file|
        data = JSON.parse(File.read(file))
        if data['datasets'].is_a?(Array)
          merged_datasets.concat(data['datasets'])
        end
      end
      
      { 'datasets' => merged_datasets }
    end
  end
end

Liquid::Template.register_filter(Jekyll::LoadDataJsonFilter)

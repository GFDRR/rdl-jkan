---
attributions:
- entity:
    affiliation: null
    email: null
    name: VIIRS satellite imagery
    url: https://data.humdata.org/dataset/electricaldistributiongridmaps
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap roads and political boundaries
    url: https://data.humdata.org/dataset/electricaldistributiongridmaps
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/electricaldistributiongridmaps
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/electricaldistributiongridmaps
dataset_id: rdls_exp-civcodngaugazmb_metad4g_electricaldistributiongri_2019
description: 'Facebook has produced a model to help map global medium voltage (MV)
  grid infrastructure, i.e. the distribution lines which connect high-voltage transmission
  infrastructure to consumer-serving low-voltage distribution. The data found here
  are model outputs for six select African countries: Malawi, Nigeria, Uganda, DRC,
  Cote D''Ivoire, and Zambia. The grid maps are produced using a new methodology that
  employs various publicly-available datasets (night time satellite imagery, roads,
  political boundaries, etc) to predict the location of existing MV grid infrastructure.
  The model documentation and code are also available , so data scientists and planners
  globally can replicate the model to expand model coverage to other countries where
  this data is not already available. You can find the model code and documentation
  here: https://github.com/facebookresearch/many-to-many-dijkstra Note: current model
  accuracy is approximately 70% when compared to existing ground-truthed data. Accuracy
  can be further improved by integrating other locally-relevant information into the
  model and running it again. Resolution: geotiff is provided at Bing Tile Level 20.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/electricaldistributiongridmaps]'
details: 'This project is no longer active and has been carried forward by others,
  mostly at the World Bank. See global estimates of grid infrastructure from this
  group here: https://gridfinder.org/'
exposure:
- asset_type:
    description: Medium voltage electrical distribution grid infrastructure mapped
      using satellite imagery and machine learning
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Monthly VIIRS satellite composites were processed with custom image
    filtering to identify consistent night-time lighting locations. These lighting
    signatures were combined with road networks and administrative boundaries as inputs
    to a machine learning model trained to predict medium voltage electrical distribution
    grid locations across six African countries.
  sources:
  - id: source_1
    license: null
    name: VIIRS satellite imagery
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: OpenStreetMap roads and political boundaries
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/electricaldistributiongridmaps
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Electrical Distribution Grid Maps (Medium-Voltage Distribution Infrastructure
    for Cote D'Ivoire)
  download_url: https://data.humdata.org/dataset/5040df47-96a2-4b3c-9a7f-2b7fb2b41316/resource/f1143ea6-0349-423d-9aeb-7eb905f5ffc8/download/electrical_grid_cote_divoire_15.csv
  format: null
  id: resource_f1143ea6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: electrical_grid_cote_divoire_15.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Medium-Voltage Distribution Infrastructure for Cote D''Ivoire Resolution:
    geotiff is provided at Bing Tile Level 20, or approximately 38m/pixel'
  download_url: https://data.humdata.org/dataset/5040df47-96a2-4b3c-9a7f-2b7fb2b41316/resource/b1d4c926-42eb-4227-b024-809302ee035f/download/electrical_grid_cote_divoire_15_electrical_distribution_grid-1.tif.zip
  format: null
  id: resource_b1d4c926
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: electrical_grid_cote_divoire_15_electrical_distribution_grid (1).tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Medium-Voltage Distribution Infrastructure for Democratic Republic
    of Congo Format: Lat/Long'
  download_url: https://data.humdata.org/dataset/5040df47-96a2-4b3c-9a7f-2b7fb2b41316/resource/90d917c8-e7c3-4192-bec4-184203bf0d0c/download/electrical_grid_democratic_republic_of_congo_15-1.csv
  format: null
  id: resource_90d917c8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: electrical_grid_democratic_republic_of_congo_15 (1).csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Medium-Voltage Distribution Infrastructure for Democratic Republic
    of Congo Resolution: geotiff is provided at Bing Tile Level 20, or approximately
    38m/pixel'
  download_url: https://data.humdata.org/dataset/5040df47-96a2-4b3c-9a7f-2b7fb2b41316/resource/a2b3a0bb-8c97-4b86-86ae-45b3f2640946/download/electrical_grid_democratic_republic_of_congo_15_electrical_distribution_grid.tif.zip
  format: null
  id: resource_a2b3a0bb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: electrical_grid_democratic_republic_of_congo_15_electrical_distribution_grid.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Electrical Distribution Grid Maps (Medium-Voltage Distribution Infrastructure
    for Malawi Format: Lat/Long)'
  download_url: https://data.humdata.org/dataset/5040df47-96a2-4b3c-9a7f-2b7fb2b41316/resource/b2b84057-9673-460f-b852-e9b3e38c5532/download/electrical_grid_malawi_15.csv
  format: null
  id: resource_b2b84057
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: electrical_grid_malawi_15.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Medium-Voltage Distribution Infrastructure for Malawi Resolution:
    geotiff is provided at Bing Tile Level 20, or approximately 38m/pixel'
  download_url: https://data.humdata.org/dataset/5040df47-96a2-4b3c-9a7f-2b7fb2b41316/resource/823d2b07-8d56-4ee2-a54a-1d5b05e9c83f/download/electrical_grid_malawi_15_electrical_distribution_grid.tif.zip
  format: null
  id: resource_823d2b07
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: electrical_grid_malawi_15_electrical_distribution_grid.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Electrical Distribution Grid Maps (Medium-Voltage Distribution Infrastructure
    for Nigeria Format: Lat/Long)'
  download_url: https://data.humdata.org/dataset/5040df47-96a2-4b3c-9a7f-2b7fb2b41316/resource/bda367ce-1888-4c84-babf-1b851ecf5592/download/electrical_grid_nigeria_15.csv
  format: null
  id: resource_bda367ce
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: electrical_grid_nigeria_15.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Medium-Voltage Infrastructure for Nigeria Resolution: geotiff is provided
    at Bing Tile Level 20, or approximately 38m/pixel'
  download_url: https://data.humdata.org/dataset/5040df47-96a2-4b3c-9a7f-2b7fb2b41316/resource/55e0416e-5c24-44c7-bb59-b90d225e801a/download/electrical_grid_nigeria_15_electrical_distribution_grid.tif.zip
  format: null
  id: resource_55e0416e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: electrical_grid_nigeria_15_electrical_distribution_grid.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Electrical Distribution Grid Maps (Medium-Voltage Distribution Infrastructure
    for Uganda Format: Lat/Long)'
  download_url: https://data.humdata.org/dataset/5040df47-96a2-4b3c-9a7f-2b7fb2b41316/resource/faea552a-bb9e-4c1c-8bf3-ba5b0136be49/download/electrical_grid_uganda_15-2.csv
  format: null
  id: resource_faea552a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: electrical_grid_uganda_15 (2).csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Medium-Voltage Distribution Infrastructure for Uganda Resolution:
    geotiff is provided at Bing Tile Level 20, or approximately 38m/pixel'
  download_url: https://data.humdata.org/dataset/5040df47-96a2-4b3c-9a7f-2b7fb2b41316/resource/f0ee4799-a345-447f-88e4-25e4d8eb6bf3/download/electrical_grid_uganda_15_electrical_distribution_grid.tif.zip
  format: null
  id: resource_f0ee4799
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: electrical_grid_uganda_15_electrical_distribution_grid.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Electrical Distribution Grid Maps (Medium-Voltage Distribution Infrastructure
    for Zambia Format: Lat/Long)'
  download_url: https://data.humdata.org/dataset/5040df47-96a2-4b3c-9a7f-2b7fb2b41316/resource/28bdc2e3-69b7-4ac6-8732-6a853f5de6af/download/electrical_grid_zambia_15.csv
  format: null
  id: resource_28bdc2e3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: electrical_grid_zambia_15.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Medium-Voltage Distribution Infrastructure for Zambia Resolution:
    geotiff is provided at Bing Tile Level 20, or approximately 38m/pixel'
  download_url: https://data.humdata.org/dataset/5040df47-96a2-4b3c-9a7f-2b7fb2b41316/resource/c5fa2453-1f52-4ad4-9696-d519e4bb4319/download/electrical_grid_zambia_15_electrical_distribution_grid.tif.zip
  format: null
  id: resource_c5fa2453
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: electrical_grid_zambia_15_electrical_distribution_grid.tif.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-civcodngaugazmb_metad4g_electricaldistributiongri_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  - NGA
  - UGA
  - CIV
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-03-19'
  start: '2019-01-24'
temporal_resolution: null
title: Electrical Distribution Grid Maps
version: null
vulnerability: null
---

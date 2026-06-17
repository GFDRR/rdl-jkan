---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: TU Delft
  url: https://data.4tu.nl/search
creator:
  affiliation: null
  email: null
  name: TU Delft
  url: https://data.4tu.nl/search
dataset_id: rdls_hzd-crstac_synthetictropicalcyclonegenerationmodelstorm_futurewindspeeds
description: 'Datasets containing tropical cyclone maximum wind speed (in m/s) return
  periods, generated using the STORM datasets under future climate conditions. Climate
  scenarios (as published): "SSP-RCP combinations" [Source: This metadata record was
  automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: strong_wind
license: CC0-1.0
lineage:
  description: Datasets generated with the synthetic resampling algorithm STORM
  sources:
  - id: source_underlying_1
    license: null
    name: IBTrACS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://github.com/NBloemendaal/STORM-return-periods
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: TU Delft
  url: https://data.4tu.nl/search
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41597-020-00720-x
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41597-020-00720-x
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/wind-related/synthetic-tropical-cyclone-generation-model-storm/future-wind-speeds/future-wind-speeds.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Synthetic Tropical cyclOne geneRation Model (STORM) - Future
    wind speeds'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/2a3759e8-f4ad-4190-abb3-434ad5c4679b
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/c460a0c8-f918-4ede-a734-75e77e99b102
  format: null
  id: resource_data-file_2
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/304d1441-bd71-47c7-8231-b20253c1cc2a
  format: null
  id: resource_data-file_3
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/856f9530-56d7-489e-8005-18ae36db4804
  format: null
  id: resource_data-file_4
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/9740b235-c2fe-4677-a8b9-f90eb13e4938
  format: null
  id: resource_data-file_5
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/df247ab2-7565-4888-b5a9-2ccd31d9c90f
  format: null
  id: resource_data-file_6
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/43ce1a8f-914a-414c-b949-884e06616301
  format: null
  id: resource_data-file_7
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/ac3fd12d-c21d-406e-8e2e-bd212ee9f817
  format: null
  id: resource_data-file_8
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/a7e915a4-ee2a-44d7-8e91-8920bff34f16
  format: null
  id: resource_data-file_9
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    - data file
- access_url: https://doi.org/10.1038/s41597-020-00720-x
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
- access_url: https://github.com/NBloemendaal/STORM-return-periods
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
    (Code link)
  download_url: null
  format: Web reference
  id: resource_link_codelink
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Code link
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_synthetictropicalcyclonegenerationmodelstorm_futurewindspeeds
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 60.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 11100
temporal:
  central_year: null
  duration: null
  end: '2050'
  start: '2015'
temporal_resolution: null
title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future wind speeds
version: null
vulnerability: null
---

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
dataset_id: rdls_hzd-crstac_synthetictropicalcyclonegenerationmodelstorm_historicalwindspeeds
description: 'Datasets containing tropical cyclone maximum wind speed (in m/s) return
  periods, generated using the STORM datasets [Source: This metadata record was automatically
  extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/wind-related/synthetic-tropical-cyclone-generation-model-storm/historical-wind-speeds/historical-wind-speeds.json
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
  title: 'STAC Item: Synthetic Tropical cyclOne geneRation Model (STORM) - Historical
    wind speeds'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Historical wind
    speeds - data file
  download_url: https://data.4tu.nl/file/0ea98bdd-5772-4da8-ae97-99735e891aff/0b98c6f5-c7af-45bb-bb6e-dac53e1b8d55
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Historical wind speeds
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Historical wind
    speeds - data file
  download_url: https://data.4tu.nl/file/0ea98bdd-5772-4da8-ae97-99735e891aff/3c839d73-e6c0-4d63-ae03-c0d05e734d57
  format: null
  id: resource_data-file_2
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Historical wind speeds
    - data file
- access_url: https://doi.org/10.1038/s41597-020-00720-x
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Historical wind
    speeds (Web reference)
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
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Historical wind
    speeds (Code link)
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
slug: rdls_hzd-crstac_synthetictropicalcyclonegenerationmodelstorm_historicalwindspeeds
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
  end: '2017'
  start: '1980'
temporal_resolution: null
title: Synthetic Tropical cyclOne geneRation Model (STORM) - Historical wind speeds
version: null
vulnerability: null
---

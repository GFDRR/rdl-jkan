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
dataset_id: rdls_hzd-crstac_synthetictropicalcyclonegenerationmodelstorm_futuretracks
description: 'Datasets consisting of 10,000 years of synthetic tropical cyclone tracks,
  generated using the Synthetic Tropical cyclOne geneRation Model (STORM) algorithm
  under future climate change. Climate scenarios (as published): "SSP-RCP combinations"
  [Source: This metadata record was automatically extracted from the STAC catalog
  climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
    url: https://github.com/NBloemendaal/STORM
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
  doi: 10.1038/s41597-020-0381-2
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41597-020-0381-2
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/wind-related/synthetic-tropical-cyclone-generation-model-storm/future-tracks/future-tracks.json
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
    tracks'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future tracks
    - data file
  download_url: https://data.4tu.nl/file/98900e17-8e01-4d70-b3b6-ca1a1da2f194/bdc3820c-7b7e-41de-8def-792f50b06c49
  format: null
  id: resource_data-file_1
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future tracks - data
    file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future tracks
    - data file
  download_url: https://data.4tu.nl/file/98900e17-8e01-4d70-b3b6-ca1a1da2f194/3b08e6a8-2824-435f-a141-9509a9922cfe
  format: null
  id: resource_data-file_2
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future tracks - data
    file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future tracks
    - data file
  download_url: https://data.4tu.nl/file/98900e17-8e01-4d70-b3b6-ca1a1da2f194/2eaeb5f6-40f3-4f94-9f9c-ca7aad3237fc
  format: null
  id: resource_data-file_3
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future tracks - data
    file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future tracks
    - data file
  download_url: https://data.4tu.nl/file/98900e17-8e01-4d70-b3b6-ca1a1da2f194/f35142d6-d858-4874-9a51-2dc08462d45f
  format: null
  id: resource_data-file_4
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future tracks - data
    file
- access_url: https://doi.org/10.1038/s41597-020-0381-2
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future tracks
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
- access_url: https://github.com/NBloemendaal/STORM
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Synthetic Tropical cyclOne geneRation Model (STORM) - Future tracks
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
slug: rdls_hzd-crstac_synthetictropicalcyclonegenerationmodelstorm_futuretracks
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
temporal_resolution: PT3H
title: Synthetic Tropical cyclOne geneRation Model (STORM) - Future tracks
version: null
vulnerability: null
---

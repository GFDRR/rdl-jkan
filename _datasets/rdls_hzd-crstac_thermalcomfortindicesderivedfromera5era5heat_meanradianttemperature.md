---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: ECMWF
  url: https://doi.org/10.24381/cds.553b7518
creator:
  affiliation: null
  email: null
  name: ECMWF
  url: https://doi.org/10.24381/cds.553b7518
dataset_id: rdls_hzd-crstac_thermalcomfortindicesderivedfromera5era5heat_meanradianttemperature
description: 'This dataset provides modelled hourly data of mean radiant temperature
  [Source: This metadata record was automatically extracted from the STAC catalog
  climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AirTemp:C
      process: extreme_heat
      trigger: null
      type: extreme_temperature
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: extreme_temperature
license: https://example.org/license/unknown
lineage:
  description: These data provide modelled hourly data for a set of indices representing
    human thermal stress and discomfort in outdoor conditions.
  sources:
  - id: source_underlying_1
    license: null
    name: ERA5
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: ECMWF
  url: https://doi.org/10.24381/cds.553b7518
purpose: data download via interface or API
referenced_by:
- author_names: null
  date_published: null
  doi: 10.24381/cds.553b7518
  id: ref_doi
  name: null
  url: https://doi.org/10.24381/cds.553b7518
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/temperature-related/thermal-comfort-indices-derived-from-era5-era5-heat/mean-radiant-temperature/mean-radiant-temperature.json
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
  title: 'STAC Item: Thermal comfort indices derived from ERA5 (ERA5-HEAT) - Mean
    radiant temperature'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Thermal comfort indices derived from ERA5 (ERA5-HEAT) - Mean radiant
    temperature - data file
  download_url: https://doi.org/10.24381/cds.553b7518
  format: null
  id: resource_data-file_1
  media_type: application/x-netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Thermal comfort indices derived from ERA5 (ERA5-HEAT) - Mean radiant temperature
    - data file
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_thermalcomfortindicesderivedfromera5era5heat_meanradianttemperature
spatial:
  bbox:
  - -180.0
  - -60.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 27750
temporal:
  central_year: null
  duration: null
  end: '2026'
  start: '1940'
temporal_resolution: PT1H
title: Thermal comfort indices derived from ERA5 (ERA5-HEAT) - Mean radiant temperature
version: null
vulnerability: null
---

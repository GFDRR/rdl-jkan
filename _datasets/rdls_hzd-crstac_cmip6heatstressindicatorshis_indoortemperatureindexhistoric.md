---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Copernicus Climate Data Store
  url: https://doi.org/10.24381/cds.776e08bd
creator:
  affiliation: null
  email: null
  name: Copernicus Climate Data Store
  url: https://doi.org/10.24381/cds.776e08bd
dataset_id: rdls_hzd-crstac_cmip6heatstressindicatorshis_indoortemperatureindexhistoric
description: 'Indoor wet-bulb globe temperature is a heat stress indicator that is
  calculated as weighted mean of wet-bulb temperature, globe temperature, and daily
  maximum temperature. In the present dataset, the influence of solar radiation and
  wind speed is not considered and wet-bulb globe temperature is calculated as weighted
  mean of wet-bulb temperature and daily maximum temperature (neglecting globe temperature).
  It thus represents indoor conditions [Source: This metadata record was automatically
  extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    extreme_temperature:
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
  event_sets_count: 1
license: https://example.org/license/unknown
lineage:
  description: The indices are provided for historical and future climate projections
    (SSP1-2.6, SSP2-4.5, SSP3-7.0, SSP5-8.5) included in the Coupled Model Intercomparison
    Project Phase 6 (CMIP6) and used in the 6th Assessment Report of the Intergovernmental
    Panel on Climate Change (IPCC).
  sources:
  - id: source_underlying_1
    license: null
    name: CMIP6
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
    url: https://github.com/IPCC-WG1/Atlas/tree/main
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Copernicus Climate Data Store
  url: https://doi.org/10.24381/cds.776e08bd
purpose: data download via interface or API (user account needed)
referenced_by:
- author_names: null
  date_published: null
  doi: 10.24381/cds.776e08bd
  id: ref_doi
  name: null
  url: https://doi.org/10.24381/cds.776e08bd
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/temperature-related/cmip6-heat-stress-indicators-his/indoor-temperature-index-historical/indoor-temperature-index-historical.json
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
  title: 'STAC Item: CMIP6 heat stress indicators (HIS) - Indoor temperature index
    historical'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: CMIP6 heat stress indicators (HIS) - Indoor temperature index historical
    - data file
  download_url: https://doi.org/10.24381/cds.776e08bd
  format: null
  id: resource_data-file_1
  media_type: application/x-netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CMIP6 heat stress indicators (HIS) - Indoor temperature index historical
    - data file
- access_url: https://github.com/IPCC-WG1/Atlas/tree/main
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CMIP6 heat stress indicators (HIS) - Indoor temperature index historical
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
slug: rdls_hzd-crstac_cmip6heatstressindicatorshis_indoortemperatureindexhistoric
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
spatial_resolution: 55500
temporal:
  central_year: null
  duration: null
  end: '2014'
  start: '1951'
temporal_resolution: P1D
title: CMIP6 heat stress indicators (HIS) - Indoor temperature index historical
version: null
vulnerability: null
---

---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Copernicus Emergency Management Service
  url: https://doi.org/10.24381/cds.2d78664e
creator:
  affiliation: null
  email: null
  name: Copernicus Emergency Management Service
  url: https://doi.org/10.24381/cds.2d78664e
dataset_id: rdls_hzd-crstac_riverdischargeglobalfloodawarenesssystemglofas_seasonalreforecasts
description: 'The dataset provides a gridded modelled time series of river discharge
  forced with seasonal range meteorological reforecasts. The data is a consistent
  representation of a key hydrological variable across the global domain, and is a
  product of the Global Flood Awareness System (GloFAS) [Source: This metadata record
  was automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://example.org/license/unknown
lineage:
  description: GloFAS datasets provide daily simulations of river discharge, covering
    the globe with the exception of Antarctica
  sources:
  - id: source_underlying_1
    license: null
    name: ECMWF SEAS5
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
  name: Copernicus Emergency Management Service
  url: https://doi.org/10.24381/cds.2d78664e
purpose: Temporal coverage up to near real-time (several months delay), with monthly
  updates.
referenced_by:
- author_names: null
  date_published: null
  doi: 10.24381/cds.0aa9b9dd
  id: ref_doi
  name: null
  url: https://doi.org/10.24381/cds.0aa9b9dd
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/flood/river-discharge-global-flood-awareness-system-glofas/seasonal-reforecasts/seasonal-reforecasts.json
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
  title: 'STAC Item: River discharge Global Flood Awareness System (GloFAS) - Seasonal
    reforecasts'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: River discharge Global Flood Awareness System (GloFAS) - Seasonal reforecasts
    - data file
  download_url: https://doi.org/10.24381/cds.0aa9b9dd
  format: null
  id: resource_data-file_1
  media_type: application/grib2
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: River discharge Global Flood Awareness System (GloFAS) - Seasonal reforecasts
    - data file
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_riverdischargeglobalfloodawarenesssystemglofas_seasonalreforecasts
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
spatial_resolution: 5550
temporal:
  central_year: null
  duration: null
  end: '2026'
  start: '1981'
temporal_resolution: P1D
title: River discharge Global Flood Awareness System (GloFAS) - Seasonal reforecasts
version: null
vulnerability: null
---

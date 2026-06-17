---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: World Resources Institute
  url: https://www.wri.org/data/aqueduct-floods-hazard-maps
creator:
  affiliation: null
  email: null
  name: World Resources Institute
  url: https://www.wri.org/data/aqueduct-floods-hazard-maps
dataset_id: rdls_hzd-crstac_floodhazardmapsaqueduct_coastalfloodsfuturescenarios
description: 'Coastal flood maps of flood extent and water depth for future scenarios.
  Climate scenarios (as published): "RCPs" [Source: This metadata record was automatically
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
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: The Aqueduct Floods Hazard Maps for riverine floods were produced using
    the GLOFRIS model with global hydrological model PCR-GLOBWB, producing long-term
    simulations of river discharges and flood levels for several climate conditions.
    Forcing was derived from the EUWATCH and ISIMIP meteorological datasets over various
    periods between 1950 and 2099. Extreme value statistics were applied to derive
    floodplain water volumes per grid cell for a set of return periods (2, 5, ...
    250, 500 years) under current climate ca. 1980 (1960-1999), in 2030 (2010-2049),
    2050 (2030-2069) and 2070 (2060-2099). The Aqueduct Floods Hazard Maps for coastal
    floods were produced using the GLOFRIS model, based on the Global Tide and Surge
    Reanalysis (GTSR) dataset and sea-level rise projections from the RISES-AM project.
    The resulting flood maps have a resolution of 30''x30''.
  sources:
  - id: source_underlying_1
    license: null
    name: GTSR
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
  name: World Resources Institute
  url: https://www.wri.org/data/aqueduct-floods-hazard-maps
purpose: data available for 2030, 2050, 2080 and RCP4.5 and 8.5
referenced_by:
- author_names: null
  date_published: null
  doi: 10.5194/nhess-20-1025-2020
  id: ref_doi
  name: null
  url: https://doi.org/10.5194/nhess-20-1025-2020
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/flood/flood-hazard-maps-aqueduct/coastal-floods-future-scenarios/coastal-floods-future-scenarios.json
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
  title: 'STAC Item: Flood hazard maps (Aqueduct) - Coastal floods future scenarios'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Flood hazard maps (Aqueduct) - Coastal floods future scenarios - data
    file
  download_url: https://www.wri.org/data/aqueduct-floods-hazard-maps
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Flood hazard maps (Aqueduct) - Coastal floods future scenarios - data file
- access_url: https://doi.org/10.5194/nhess-20-1025-2020
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood hazard maps (Aqueduct) - Coastal floods future scenarios (Web
    reference)
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
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_floodhazardmapsaqueduct_coastalfloodsfuturescenarios
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 926
temporal:
  central_year: null
  duration: null
  end: '2080'
  start: '2030'
temporal_resolution: null
title: Flood hazard maps (Aqueduct) - Coastal floods future scenarios
version: null
vulnerability: null
---

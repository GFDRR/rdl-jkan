---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: ECMWF
  url: https://doi.org/10.24381/cds.b9c753f1
creator:
  affiliation: null
  email: null
  name: ECMWF
  url: https://doi.org/10.24381/cds.b9c753f1
dataset_id: rdls_hzd-crstac_seasonalforecastoffiredangerindices_australianmcarthur
description: 'Australian McArthur (Mark 5) Rating System at 1 dec deg spatial resolution.
  Components: Drought factor, Keetch-Byram drougth index, Fire danger index [Source:
  This metadata record was automatically extracted from the STAC catalog climate-risk-stac
  (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
      intensity_measure: burnedarea:ha
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: wildfire
license: https://example.org/license/unknown
lineage:
  description: Modelled daily fire danger time series, driven by seasonal weather
    forecasts (ECMWF SEAS5) and using fire danger indices from the U.S. Forest Service
    National Fire-Danger Rating System (NFDRS), the Canadian Forest Service Fire Weather
    Index Rating System (FWI), and the Australian McArthur (Mark 5) rating systems.
  sources:
  - id: source_underlying_1
    license: null
    name: ECMWF SEAS5
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
    url: https://github.com/fdg10371/Jupyter_notebooks
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: ECMWF
  url: https://doi.org/10.24381/cds.b9c753f1
purpose: data download via interface or API
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41597-024-02948-3
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41597-024-02948-3
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/environmental/seasonal-forecast-of-fire-danger-indices/australian-mcarthur/australian-mcarthur.json
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
  title: 'STAC Item: Seasonal forecast of fire danger indices - Australian McArthur'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Seasonal forecast of fire danger indices - Australian McArthur - data
    file
  download_url: https://doi.org/10.24381/cds.b9c753f1
  format: null
  id: resource_data-file_1
  media_type: application/grib
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Seasonal forecast of fire danger indices - Australian McArthur - data file
- access_url: https://doi.org/10.1038/s41597-024-02948-3
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Seasonal forecast of fire danger indices - Australian McArthur (Web
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
- access_url: https://github.com/fdg10371/Jupyter_notebooks
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Seasonal forecast of fire danger indices - Australian McArthur (Code
    link)
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
slug: rdls_hzd-crstac_seasonalforecastoffiredangerindices_australianmcarthur
spatial:
  bbox:
  - -179.95
  - -89.95
  - 179.95
  - 89.95
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 111000
temporal:
  central_year: null
  duration: null
  end: '2026'
  start: '1981'
temporal_resolution: P1D
title: Seasonal forecast of fire danger indices - Australian McArthur
version: null
vulnerability: null
---

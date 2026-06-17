---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: ECMWF
  url: https://doi.org/10.24381/cds.0e89c522
creator:
  affiliation: null
  email: null
  name: ECMWF
  url: https://doi.org/10.24381/cds.0e89c522
dataset_id: rdls_hzd-crstac_historicalreconstructionoffiredangerindices_australianmcarthur
description: 'Australian McArthur (Mark 5) Rating System at 0.25 dec deg spatial resolution.
  Components: Drought factor, Keetch-Byram drougth index, Fire danger index [Source:
  This metadata record was automatically extracted from the STAC catalog climate-risk-stac
  (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
  description: The data set provides complete historical reconstruction of meteorological
    conditions favourable to the start, spread and sustainability of fires. The fire
    danger metrics provided are part of a vast dataset produced by the Copernicus
    Emergency Management Service for the European Forest Fire Information System (EFFIS).
  sources:
  - id: source_underlying_1
    license: null
    name: ECMWF ERA5
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
  url: https://doi.org/10.24381/cds.0e89c522
purpose: data download via interface or API
referenced_by:
- author_names: null
  date_published: null
  doi: 10.24381/cds.0e89c522
  id: ref_doi
  name: null
  url: https://doi.org/10.24381/cds.0e89c522
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/environmental/historical-reconstruction-of-fire-danger-indices/australian-mcarthur/australian-mcarthur.json
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
  title: 'STAC Item: Historical reconstruction of fire danger indices - Australian
    McArthur'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Historical reconstruction of fire danger indices - Australian McArthur
    - data file
  download_url: https://doi.org/10.24381/cds.0e89c522
  format: null
  id: resource_data-file_1
  media_type: application/grib2
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Historical reconstruction of fire danger indices - Australian McArthur -
    data file
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_historicalreconstructionoffiredangerindices_australianmcarthur
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
spatial_resolution: 27750
temporal:
  central_year: null
  duration: null
  end: '2026'
  start: '1940'
temporal_resolution: P1D
title: Historical reconstruction of fire danger indices - Australian McArthur
version: null
vulnerability: null
---

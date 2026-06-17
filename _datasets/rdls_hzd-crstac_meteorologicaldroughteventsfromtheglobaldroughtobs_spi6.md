---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Global Drought Observatory
  url: https://data.jrc.ec.europa.eu/collection/id-00321
creator:
  affiliation: null
  email: null
  name: Global Drought Observatory
  url: https://data.jrc.ec.europa.eu/collection/id-00321
dataset_id: rdls_hzd-crstac_meteorologicaldroughteventsfromtheglobaldroughtobs_spi6
description: 'Drought events based on Standard Precipitation Index of 6 Months [Source:
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
      intensity_measure: spi:dimensionless
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: drought
license: CC-BY-4.0
lineage:
  description: More than 4500 drought events classified using a few indicators as
    the SPI and the SPEI at different temporal scales. The database of drought events
    has specific entries for each macro-region and country.
  sources:
  - id: source_underlying_1
    license: null
    name: GPCC
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_2
    license: null
    name: CRU TS
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
  name: Global Drought Observatory
  url: https://data.jrc.ec.europa.eu/collection/id-00321
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1016/j.ejrh.2019.100593
  id: ref_doi
  name: null
  url: https://doi.org/10.1016/j.ejrh.2019.100593
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/precipitation-related/meteorological-drought-events-from-the-global-drought-observatory-gdo/spi6/spi6.json
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
  title: 'STAC Item: Meteorological drought events from the Global Drought Observatory
    (GDO) - SPI6'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Meteorological drought events from the Global Drought Observatory (GDO)
    - SPI6 - data file
  download_url: https://data.jrc.ec.europa.eu/collection/id-00321
  format: null
  id: resource_data-file_1
  media_type: application/x-netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Meteorological drought events from the Global Drought Observatory (GDO) -
    SPI6 - data file
- access_url: https://doi.org/10.1016/j.ejrh.2019.100593
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Meteorological drought events from the Global Drought Observatory (GDO)
    - SPI6 (Web reference)
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
slug: rdls_hzd-crstac_meteorologicaldroughteventsfromtheglobaldroughtobs_spi6
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
spatial_resolution: 55500
temporal:
  central_year: null
  duration: null
  end: '2016'
  start: '1951'
temporal_resolution: P1M
title: Meteorological drought events from the Global Drought Observatory (GDO) - SPI6
version: null
vulnerability: null
---

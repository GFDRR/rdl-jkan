---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: JRC Data Catalogue
  url: https://data.jrc.ec.europa.eu/collection/id-0054
creator:
  affiliation: null
  email: null
  name: JRC Data Catalogue
  url: https://data.jrc.ec.europa.eu/collection/id-0054
dataset_id: rdls_hzd-crstac_jrcfloodhazardmaps_jrcfloodhazardmapsglobal
description: 'The datasets included in this collection depict flood prone areas in
  the World for river flood events of different magnitude, i.e. different six return
  periods from 1-in-10-year to 1-in-500-year events. The maps have been developed
  using hydrological and hydrodynamic models, driven by the climatological data of
  the Global Flood Awareness Systems (GloFAS) [Source: This metadata record was automatically
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
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: The datasets included in this collection depict flood prone areas in
    Europe and the World for river flood events of different magnitude, i.e. different
    six return periods from 1-in-10-year to 1-in-500-year events. The maps have been
    developed using hydrological and hydrodynamic models, driven by the climatological
    data of the European and Global Flood Awareness Systems (EFAS and GloFAS). European-scale
    maps comprise most of the geographical Europe and all the river basins entering
    the Mediterranean and Black Seas in the Caucasus, Middle East and Northern Africa
    countries.
  sources:
  - id: source_underlying_1
    license: null
    name: several data sources (see publication for further details)
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
  name: JRC Data Catalogue
  url: https://data.jrc.ec.europa.eu/collection/id-0054
purpose: Cell values indicate water depth (in m), based on an analysis from 2000-2013
  (so roughly representing 2013)
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1016/j.advwatres.2016.05.002
  id: ref_doi
  name: null
  url: https://doi.org/10.1016/j.advwatres.2016.05.002
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/flood/jrc-flood-hazard-maps/jrc-flood-hazard-maps-global/jrc-flood-hazard-maps-global.json
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
  title: 'STAC Item: JRC flood hazard maps global'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: JRC flood hazard maps global - data file
  download_url: https://cidportal.jrc.ec.europa.eu/ftp/jrc-opendata/FLOODS/GlobalMaps/floodMapGL_rp10y.zip
  format: null
  id: resource_data-file_1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JRC flood hazard maps global - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: JRC flood hazard maps global - data file
  download_url: https://cidportal.jrc.ec.europa.eu/ftp/jrc-opendata/FLOODS/GlobalMaps/floodMapGL_rp20y.zip
  format: null
  id: resource_data-file_2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JRC flood hazard maps global - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: JRC flood hazard maps global - data file
  download_url: https://cidportal.jrc.ec.europa.eu/ftp/jrc-opendata/FLOODS/GlobalMaps/floodMapGL_rp50y.zip
  format: null
  id: resource_data-file_3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JRC flood hazard maps global - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: JRC flood hazard maps global - data file
  download_url: https://cidportal.jrc.ec.europa.eu/ftp/jrc-opendata/FLOODS/GlobalMaps/floodMapGL_rp100y.zip
  format: null
  id: resource_data-file_4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JRC flood hazard maps global - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: JRC flood hazard maps global - data file
  download_url: https://cidportal.jrc.ec.europa.eu/ftp/jrc-opendata/FLOODS/GlobalMaps/floodMapGL_rp200y.zip
  format: null
  id: resource_data-file_5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JRC flood hazard maps global - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: JRC flood hazard maps global - data file
  download_url: https://cidportal.jrc.ec.europa.eu/ftp/jrc-opendata/FLOODS/GlobalMaps/floodMapGL_rp500y.zip
  format: null
  id: resource_data-file_6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JRC flood hazard maps global - data file
- access_url: https://doi.org/10.1016/j.advwatres.2016.05.002
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: JRC flood hazard maps global (Web reference)
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
slug: rdls_hzd-crstac_jrcfloodhazardmaps_jrcfloodhazardmapsglobal
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
  end: '2013'
  start: '2013'
temporal_resolution: null
title: JRC flood hazard maps global
version: null
vulnerability: null
---

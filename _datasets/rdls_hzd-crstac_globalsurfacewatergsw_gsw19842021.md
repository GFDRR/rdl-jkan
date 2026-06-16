---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: EC JRC, Google
  url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GSWE/
creator:
  affiliation: null
  email: null
  name: EC JRC, Google
  url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GSWE/
dataset_id: rdls_hzd-crstac_globalsurfacewatergsw_gsw19842021
description: 'The dataset includes the occurrence, seasonality, recurrence, transitions,
  and maximum water extent for different temporal moment at global scale [Source:
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: The dataset includes the occurrence, seasonality, recurrence, transitions,
    and maximum water extent for different temporal moment at global scale
  sources:
  - id: source_underlying_1
    license: null
    name: precessed from Landsat
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_2
    license: null
    name: SRTM DEM
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_3
    license: null
    name: GTOPO30 DEM
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_4
    license: null
    name: GMTED2010
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_5
    license: null
    name: GHSL
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_6
    license: null
    name: GADM
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
    url: https://github.com/mentaljam/download_water_data
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: EC JRC, Google
  url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GSWE/
purpose: several aggregation levels and download options available
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/nature20584
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/nature20584
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/flood/global-surface-water-gsw/gsw-1984-2021/gsw-1984-2021.json
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
  title: 'STAC Item: Global Surface Water (GSW) - GSW 1984-2021'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Surface Water (GSW) - GSW 1984-2021 - data file
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GSWE/
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Surface Water (GSW) - GSW 1984-2021 - data file
- access_url: https://doi.org/10.1038/nature20584
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Surface Water (GSW) - GSW 1984-2021 (Web reference)
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
- access_url: https://github.com/mentaljam/download_water_data
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Surface Water (GSW) - GSW 1984-2021 (Code link)
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
slug: rdls_hzd-crstac_globalsurfacewatergsw_gsw19842021
spatial:
  bbox:
  - -180.0
  - -56.0
  - 180.0
  - 78.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 31
temporal:
  central_year: null
  duration: null
  end: '2021'
  start: '1984'
temporal_resolution: P1M
title: Global Surface Water (GSW) - GSW 1984-2021
version: null
vulnerability: null
---

---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: science@axaclimate.com
  name: AXA Climate
  url: null
creator:
  affiliation: null
  email: null
  name: AXA Climate
  url: https://climate.axa
dataset_id: rdls_hzd-mdg_grma_pm10dustproxy
description: This dataset provides the sub-daily atmospheric concentrations of particulate
  matter with a diameter smaller than 10 micrometers (PM10).
details: "This dataset is used as a proxy for dust storms occurence, it is extracted\
  \ over Madagascar from the CAMS global reanalysis EAC4 (ECMWF Atmospheric Composition\
  \ Reanalysis 4) at a 0.75\xB0 resolution, available from 2003 to 2023 (Inness et\
  \ al., 2019). Daily average values were computed to produce the statistics."
exposure: []
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: empirical
      calculation_method: inferred
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_dust_001
        intensity_measure: MHI:-
        process: extratropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_dust_001
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: GRMA Madagascar - Phase 1
  url: https://www.resiliencemada.gov.mg
publisher:
  affiliation: null
  email: null
  name: Global Risk Modelling Alliance
  url: https://grma.global
purpose: This dataset was developed during the first phase of GRMA's project in Madagascar.
  This project aimed at updating Madagascar's risk profile, and see the risk evolution
  under climate change.
referenced_by:
- author_names:
  - "Inness, A., Ades, M., Agust\xED-Panareda, A., Barr\xE9, J., Benedictow, A., Blechschmidt,\
    \ A.-M., Dominguez, J. J., Engelen, R., Eskes, H., Flemming, J., Huijnen, V.,\
    \ Jones, L., Kipling, Z., Massart, S., Parrington, M., Peuch, V.-H., Razinger,\
    \ M., Remy, S., Schulz, M., and Suttie, M."
  date_published: null
  doi: https://doi.org/10.5194/acp-19-3515-2019
  id: reference_bguYe1Yo
  name: The CAMS reanalysis of atmospheric composition
  url: https://acp.copernicus.org/articles/19/3515/2019/
resources:
- access_url: https://ads.atmosphere.copernicus.eu/datasets/cams-global-reanalysis-eac4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: CAMS global reanalysis EAC4 (ECMWF Atmospheric Composition Reanalysis
    4) in netcdf format.
  download_url: https://ads.atmosphere.copernicus.eu/datasets/cams-global-reanalysis-eac4
  format: null
  id: resource_jb84s2Hu
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 75000
  temporal:
    central_year: null
    duration: null
    end: '2023'
    start: '2003'
  temporal_resolution: null
  title: CAMS Reanalysis
- access_url: https://www.resiliencemada.gov.mg/catalogue/#/dataset/1162
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: High resolution land cover from ESA's WorldCover data v200. The field
    crops grid points are extracted to describe agricultural regions that could be
    exposed to Tiomena.
  download_url: https://www.resiliencemada.gov.mg/catalogue/#/dataset/1162
  format: null
  id: resource_ouyEI56f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10
  temporal:
    central_year: null
    duration: null
    end: '2021'
    start: '2021'
  temporal_resolution: null
  title: Crops location
- access_url: https://www.worldpop.org/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: WordPop population count dataset for Madagascar (2020). The original
    dataset was aggregated to 10km resolution.
  download_url: https://www.worldpop.org/
  format: null
  id: resource_eIpuXA7j
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: 10km resolution grid cells
  spatial_resolution: 10000
  temporal:
    central_year: null
    duration: null
    end: '2020'
    start: '2020'
  temporal_resolution: null
  title: Population exposure dataset
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mdg_grma_pm10dustproxy
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Tiomena Particulate Matter PM10 (CAMS)
version: '1.0'
vulnerability: null
---

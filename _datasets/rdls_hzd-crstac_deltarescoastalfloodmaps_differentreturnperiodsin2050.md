---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Deltares
  url: https://planetarycomputer.microsoft.com/dataset/deltares-floods
creator:
  affiliation: null
  email: null
  name: Deltares
  url: https://planetarycomputer.microsoft.com/dataset/deltares-floods
dataset_id: rdls_hzd-crstac_deltarescoastalfloodmaps_differentreturnperiodsin2050
description: 'Inundation (m) of coastal floods at 3 arc seconds resolution for 2050
  (return periods 0, 2, 5, 10, 25, 50, 100, 250). Climate scenarios (as published):
  "RCPs" [Source: This metadata record was automatically extracted from the STAC catalog
  climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
license: https://spdx.org/licenses/CDLA-Permissive-1.0.html
lineage:
  description: Global flood maps are simulated based on coastal extreme water levels
    with given return periods. These coastal water levels are taken from the Deltares
    dataset of extreme sea levels modelled using GTSMv3.0 with ERA5 reanalysis dataset
    (1979-2018) used a atmospheric forcing. Global coastal flood maps are simulated
    based on two DEMs (i.e. MERIT, NASADEM) and are available at high resolution of
    3 arc-seconds (90m at the equator). A bathtub inundation model that includes flood
    attenuation and roughness is used as the flood modeling tool. Spatial fields of
    sea level rise were imposed on extreme water levels, which were derived for the
    present-day situation (2018, end of the ERA5 climate reanalysis) and for the future
    situation (2050, based on the IPCC AR5 assessment for the RCP 8.5 scenario).
  sources:
  - id: source_underlying_1
    license: null
    name: GTSM
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_2
    license: null
    name: MERIT-DEM
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_3
    license: null
    name: NASADEM
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_4
    license: null
    name: ERA5
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
    url: https://planetarycomputer.microsoft.com/dataset/deltares-floods#Example-Notebook
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Deltares
  url: https://planetarycomputer.microsoft.com/dataset/deltares-floods
purpose: download via API (example provided), data available for RCP8.5
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_pub_publicationlink
  name: Publication link
  url: https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_docs/11206409-003-ZWS-0003_v0.1-Planetary-Computer-Deltares-global-flood-docs.pdf
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/flood/deltares-coastal-flood-maps/different-return-periods-in-2050/different-return-periods-in-2050.json
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
  title: 'STAC Item: Deltares Coastal Flood Maps - Different return periods in 2050'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Deltares Coastal Flood Maps - Different return periods in 2050 - data
    file
  download_url: https://planetarycomputer.microsoft.com/dataset/deltares-floods
  format: null
  id: resource_data-file_1
  media_type: application/x-netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Deltares Coastal Flood Maps - Different return periods in 2050 - data file
- access_url: https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_docs/11206409-003-ZWS-0003_v0.1-Planetary-Computer-Deltares-global-flood-docs.pdf
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Deltares Coastal Flood Maps - Different return periods in 2050 (Publication
    link)
  download_url: null
  format: Web reference
  id: resource_link_publicationlink
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Publication link
- access_url: https://planetarycomputer.microsoft.com/dataset/deltares-floods#Example-Notebook
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Deltares Coastal Flood Maps - Different return periods in 2050 (Code
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
slug: rdls_hzd-crstac_deltarescoastalfloodmaps_differentreturnperiodsin2050
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
spatial_resolution: 93
temporal:
  central_year: null
  duration: null
  end: '2050'
  start: '2050'
temporal_resolution: null
title: Deltares Coastal Flood Maps - Different return periods in 2050
version: null
vulnerability: null
---

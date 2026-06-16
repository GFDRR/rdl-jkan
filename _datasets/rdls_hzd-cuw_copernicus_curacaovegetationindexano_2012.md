---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/cuw-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/cuw-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/cuw-anomalies-fapar-viirs
dataset_id: rdls_hzd-cuw_copernicus_curacaovegetationindexano_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/cuw-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: FAPAR:-
      process: agricultural_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: FAPAR values from VIIRS satellite observations are composited at 10-day
    intervals. Anomalies are calculated at each grid cell as the deviation from a
    long-term mean baseline (2012 to the last available full year), producing raster
    datasets suitable for agricultural drought detection and vegetation health monitoring.
  sources:
  - id: source_1
    license: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cuw-anomalies-fapar-viirs
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://drought.emergency.copernicus.eu/data/factsheets/factsheet_fapar_viirs.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2026-01-01 to 2026-01-10)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/35b29337-d627-4ee7-ab59-92edd2c675a3/download/cuw_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_35b29337
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2025-01-01 to 2025-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/ceba7f13-70f5-4d64-88d4-d4c79df4575b/download/cuw_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_ceba7f13
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2024-01-01 to 2024-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/8f5027a1-0a91-4c8f-ad68-4fee9d7aa2e8/download/cuw_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_8f5027a1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2023-01-01 to 2023-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/45fdd744-dcc7-4e0d-8b90-98d81c9ef1cf/download/cuw_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_45fdd744
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2022-01-01 to 2022-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/30dcb8b3-7284-4813-b167-5c29c0154264/download/cuw_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_30dcb8b3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2021-01-01 to 2021-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/9be6bb47-3160-461d-a93b-0c632a2ae513/download/cuw_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_9be6bb47
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2020-01-01 to 2020-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/662c14d6-cbdf-46f4-b28a-058dcd688233/download/cuw_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_662c14d6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2019-01-01 to 2019-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/1f5507d7-c8ab-4bb9-9eac-0253fe038167/download/cuw_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_1f5507d7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2018-01-01 to 2018-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/2b27237c-d2ff-473f-9f60-868bc574787f/download/cuw_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_2b27237c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2017-01-01 to 2017-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/9cb6df47-74b7-4cee-83c7-02e35f7cef75/download/cuw_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_9cb6df47
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2016-01-01 to 2016-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/59b8e72e-fa8b-487a-9a6b-cc862ee7e547/download/cuw_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_59b8e72e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2015-01-01 to 2015-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/13806661-af66-4c7f-9078-9c0423cc8167/download/cuw_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_13806661
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2014-01-01 to 2014-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/20bb3d28-d750-4c3b-a384-cffa4d5d971f/download/cuw_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_20bb3d28
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2013-01-01 to 2013-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/ef69b136-0989-4a9d-98f1-116722cbc6e8/download/cuw_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_ef69b136
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2012-01-21 to 2012-12-31)"
  download_url: https://data.humdata.org/dataset/ad10cb26-eaa0-48bd-b2b5-152ba38b6947/resource/eedc1f93-3606-4201-a2f6-941f13be06b4/download/cuw_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_eedc1f93
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-cuw_copernicus_curacaovegetationindexano_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - CUW
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: "Cura\xE7ao: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)"
version: null
vulnerability: null
---

---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/mus-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Visible Infrared Imaging Radiometer Suite (VIIRS)
    url: https://data.humdata.org/dataset/mus-anomalies-fapar-viirs
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/mus-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/mus-anomalies-fapar-viirs
dataset_id: rdls_hzd-mus_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/mus-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: SPI:-
        process: agricultural_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FAPAR values are derived from 10-day composite VIIRS satellite imagery
    by the JRC Global Drought Observatory. Anomalies are computed at each grid cell
    as deviations from the long-term mean baseline spanning 2012 to the most recent
    complete year. The resulting raster time series serves as an indicator of agricultural
    drought stress on vegetation productivity in Mauritius.
  sources:
  - id: source_1
    license: null
    name: European Commission, Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Visible Infrared Imaging Radiometer Suite (VIIRS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mus-anomalies-fapar-viirs
  rel: source
loss:
  losses: []
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
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/1f3ec721-a4d5-4518-b051-f126558bf9d0/download/mus_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_1f3ec721
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/75295f37-602c-4429-a8fd-9d8a2a678882/download/mus_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_75295f37
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/41e6549a-3b82-4bd8-9355-8de39d6dbe6c/download/mus_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_41e6549a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/75a26f9d-2901-445b-998b-b833c061483f/download/mus_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_75a26f9d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/2c173bc2-7d73-4d59-8bce-3b06c62c8041/download/mus_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_2c173bc2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/234b5578-69f4-4bab-a8ea-f36c53fb70fe/download/mus_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_234b5578
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/a348eedf-ac49-4c68-93a9-1a5ff564cb34/download/mus_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_a348eedf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/eeba921d-3c4d-43e2-b97d-31410052fc10/download/mus_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_eeba921d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/9560e9e3-0b28-446f-a75d-afb84fdc3ef7/download/mus_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_9560e9e3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/563d45cd-930a-4928-b7ba-91e747b497ca/download/mus_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_563d45cd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/894dcf39-a1c1-489e-bb86-404faf9171d8/download/mus_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_894dcf39
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/27e58507-08c4-4426-93da-1ca258081764/download/mus_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_27e58507
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/cceccba6-fe43-40fe-8170-6eef2e3e1692/download/mus_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_cceccba6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/74b7771b-791e-4ee3-b023-cd603cea1ea4/download/mus_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_74b7771b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/039bed6d-1ea9-4641-b1c1-e21cb1b49ba9/resource/c590bb4f-7e1f-44cb-90c1-2a8a59be6e69/download/mus_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_c590bb4f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mus_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mus_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - MUS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Mauritius: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---

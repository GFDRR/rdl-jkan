---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Myanmar Information Management Unit (MIMU)
  url: https://data.humdata.org/dataset/mimu-geonode-sluice-gates-in-myanmar
creator:
  affiliation: null
  email: null
  name: Myanmar Information Management Unit (MIMU)
  url: https://data.humdata.org/dataset/mimu-geonode-sluice-gates-in-myanmar
dataset_id: rdls_exp-mmr_mimu_sluicegates_20250114
description: 'Non-authoritative dataset of >300 sluice gates (with geographic coordiates
  for 274 sluice gates) in Myanmar. A sluice gate is a water control structure used
  to regulate the flow of water in rivers, canals, and irrigation systems. In agricultural
  settings, especially for large areas, sluice gates are vital for managing water
  levels, preventing flooding, and ensuring adequate irrigation. They are typically
  adjustable, allowing farmers to control water flow, direct it to fields, or block
  it to prevent water damage during storms or heavy rains. For Myanmar, esp. in the
  low lying delta areas installed, sluice gates are essential to protect farmland
  from flooding. Dataset produced by CDE Myanmar based on publicly available reference
  date (esp. GAD Township profiles 2019 and IWUMD website), enhanced with local knowledge
  and determining geographic coordinates using mostly large scale satellite/google
  satellite. Attribute data available for most sluice dates include - the river/stream
  name the sluice gate provides protection from - the size of the gate - the construction
  material - the construcction period (year of start & completion) - the size of the
  protected area - Township name Creation methodology: - create excel masterlist from
  GAD and IWUMD, incl. attributes and assign unique code. - based on the reference
  data location maps and textual location information, identification of sluice gate
  cooridinates on Google/Bing imagery. - addition of sluice gate data based on local
  knowledge - cleanup of data, standardization of attributes and correcting typos
  Known issues: - dataset may be out of date (GAD township profiles from 2019, IWUMD
  data from 2023) - for 65 (out of 339 known sluice gates) no geographic coordinates
  could be determined - for 42 sluice gates, the geographic coordinates are ''best-guess'',
  meaning that there is a possibility that the reference data from GAD/IWUMD and the
  sluice gate identified in google/bing imagery may not indicate the same sluice gate
  - reference data from GAD and IWUMD may be incomplete, thus leading to missing sluice
  gates in this dataset - for some sluice gates, attribute data is missing or incomplete
  - some sluice gates may be non-functional or destroyed Spatial dataset created based
  on 1:5.000 - 1:2.000 scaled imagery.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mimu-geonode-sluice-gates-in-myanmar]'
details: "This product has been prepared for operational purposes only, to support\
  \ humanitarian and development activities in Myanmar. Copyright \xC2\xA92020 Myanmar\
  \ Information Management Unit. MIMU geospatial datasets cannot be used on online\
  \ platform unless with prior written agreement from MIMU. MIMU products are not\
  \ for sale and can be used free of charge with attribution. For more information\
  \ see http://themimu.info/mimu-terms-conditions."
exposure:
- asset_type:
    description: Point locations of sluice gates (water control structures) used for
      flood management and irrigation in Myanmar, with geographic coordinates for
      274 of over 300 recorded gates
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Sluice gate locations were compiled by MIMU from available reference
    sources into a non-authoritative point dataset covering Myanmar, with geographic
    coordinates recorded for 274 of over 300 identified structures. The dataset is
    intended to support flood management and agricultural water control planning,
    particularly in delta regions prone to flooding.
  sources:
  - id: source_1
    license: null
    name: Myanmar Information Management Unit (MIMU)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mimu-geonode-sluice-gates-in-myanmar
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://geonode.themimu.info/geoserver/geonode/ows?format_options=charset%3AUTF-8&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature&typename=geonode:mm_sluicegates_cde_pt_v20250101
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'Zipped Shapefile. Non-authoritative dataset of >300 sluice gates (with
    geographic coordiates for 274 sluice gates) in Myanmar. A sluice gate is a water
    control structure used to regulate the flow of water in rivers, canals, and irrigation
    systems. In agricultural settings, especially for large areas, sluice gates are
    vital for managing water levels, preventing flooding, and ensuring adequate irrigation.
    They are typically adjustable, allowing farmers to control water flow, direct
    it to fields, or block it to prevent water damage during storms or heavy rains.
    For Myanmar, esp. in the low lying delta areas installed, sluice gates are essential
    to protect farmland from flooding. Dataset produced by CDE Myanmar based on publicly
    available reference date (esp. GAD Township profiles 2019 and IWUMD website),
    enhanced with local knowledge and determining geographic coordinates using mostly
    large scale satellite/google satellite. Attribute data available for most sluice
    dates include - the river/stream name the sluice gate provides protection from
    - the size of the gate - the construction material - the construcction period
    (year of start & completion) - the size of the protected area - Township name
    Creation methodology: - create excel masterlist from GAD and IWUMD, incl. attributes
    and assign unique code. - based on the reference data location maps and textual
    location information, identification of sluice gate cooridinates on Google/Bing
    imagery. - addition of sluice gate data based on local knowledge - cleanup of
    data, standardization of attributes and correcting typos Known issues: - dataset
    may be out of date (GAD township profiles from 2019, IWUMD data from 2023) - for
    65 (out of 339 known sluice gates) no geographic coordinates could be determined
    - for 42 sluice gates, the geographic coordinates are ''best-guess'', meaning
    that there is a possibility that the reference data from GAD/IWUMD and the sluice
    gate identified in google/bing imagery may not indicate the same sluice gate -
    reference data from GAD and IWUMD may be incomplete, thus leading to missing sluice
    gates in this dataset - for some sluice gates, attribute data is missing or incomplete
    - some sluice gates may be non-functional or destroyed'
  download_url: null
  format: null
  id: resource_53a6c90a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sluice Gates in Myanmar shapefile
- access_url: https://geonode.themimu.info/geoserver/geonode/ows?service=WFS&version=1.0.0&request=GetFeature&outputFormat=application%2Fjson&typeName=geonode:mm_sluicegates_cde_pt_v20250101
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'GeoJSON file. Non-authoritative dataset of >300 sluice gates (with
    geographic coordiates for 274 sluice gates) in Myanmar. A sluice gate is a water
    control structure used to regulate the flow of water in rivers, canals, and irrigation
    systems. In agricultural settings, especially for large areas, sluice gates are
    vital for managing water levels, preventing flooding, and ensuring adequate irrigation.
    They are typically adjustable, allowing farmers to control water flow, direct
    it to fields, or block it to prevent water damage during storms or heavy rains.
    For Myanmar, esp. in the low lying delta areas installed, sluice gates are essential
    to protect farmland from flooding. Dataset produced by CDE Myanmar based on publicly
    available reference date (esp. GAD Township profiles 2019 and IWUMD website),
    enhanced with local knowledge and determining geographic coordinates using mostly
    large scale satellite/google satellite. Attribute data available for most sluice
    dates include - the river/stream name the sluice gate provides protection from
    - the size of the gate - the construction material - the construcction period
    (year of start & completion) - the size of the protected area - Township name
    Creation methodology: - create excel masterlist from GAD and IWUMD, incl. attributes
    and assign unique code. - based on the reference data location maps and textual
    location information, identification of sluice gate cooridinates on Google/Bing
    imagery. - addition of sluice gate data based on local knowledge - cleanup of
    data, standardization of attributes and correcting typos Known issues: - dataset
    may be out of date (GAD township profiles from 2019, IWUMD data from 2023) - for
    65 (out of 339 known sluice gates) no geographic coordinates could be determined
    - for 42 sluice gates, the geographic coordinates are ''best-guess'', meaning
    that there is a possibility that the reference data from GAD/IWUMD and the sluice
    gate identified in google/bing imagery may not indicate the same sluice gate -
    reference data from GAD and IWUMD may be incomplete, thus leading to missing sluice
    gates in this dataset - for some sluice gates, attribute data is missing or incomplete
    - some sluice gates may be non-functional or destroyed'
  download_url: null
  format: null
  id: resource_8707bc63
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sluice Gates in Myanmar geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mmr_mimu_sluicegates_20250114
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-01-14'
temporal_resolution: null
title: Sluice Gates in Myanmar
version: null
vulnerability: null
---

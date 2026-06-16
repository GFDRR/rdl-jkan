---
attributions:
- entity:
    affiliation: null
    email: null
    name: GAD 2019 township profiles
    url: https://data.humdata.org/dataset/mimu-geonode-bridges-180ft-in-myanmar
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Local knowledge
    url: https://data.humdata.org/dataset/mimu-geonode-bridges-180ft-in-myanmar
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: High resolution satellite imagery
    url: https://data.humdata.org/dataset/mimu-geonode-bridges-180ft-in-myanmar
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Myanmar Information Management Unit (MIMU)
  url: https://data.humdata.org/dataset/mimu-geonode-bridges-180ft-in-myanmar
creator:
  affiliation: null
  email: null
  name: Myanmar Information Management Unit (MIMU)
  url: https://data.humdata.org/dataset/mimu-geonode-bridges-180ft-in-myanmar
dataset_id: rdls_exp-mmr_mimu_bridges180ft_20240301
description: 'Point location dataset of larger bridges (>180ft) in Myanmar. Co-produced
  by CDE & MIMU based on tabular data in GAD 2019 township profiles and local knowledge
  using mostly large scale satellite imagery to identify geographic location. Dataset
  of >850 larger bridges (>180 ft length) listed in GADs 2019 township profiles and
  >270 additional bridges based on local knowledge. For over 980 of those, centerpoint
  geographic coordinates were identified and added to this dataset using mostly high
  resolution satellite imagery. Bridge data (bridges >180ft) extracted from all GAD
  2019 township profiles to an excel master list. Identification of geographic coordinate
  based on bridge name & location description data, high res. Satellite information
  (and local knowledge) Adding of some smaller bridges from GAD 2019 township profiles
  and based on local knowledge. Master data in excel and bridge location shapefile.
  ArcGIS tool to combine, filter and export a cleaned product for public sharing.
  Known issues: - Wa state townships not included as no GAD township profiles 2019
  covering those areas available. - For some bridges no location was found - Location
  data based on best-guess approach (descriptive info & imagery) - some bridges might
  not be fully functional or damaged in 2024 - many bridges (mostly for those not
  listed in the GAD township profiles) lack name information - some attribute data
  (length, year built etc.) is missing/has not been included in the excel master list
  for bridges listed in GAD township profiles for which no coordinates were identified.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mimu-geonode-bridges-180ft-in-myanmar]'
details: "This product has been prepared for operational purposes only, to support\
  \ humanitarian and development activities in Myanmar. Copyright \xC2\xA92020 Myanmar\
  \ Information Management Unit. MIMU geospatial datasets cannot be used on online\
  \ platform unless with prior written agreement from MIMU. MIMU products are not\
  \ for sale and can be used free of charge with attribution. For more information\
  \ see http://themimu.info/mimu-terms-conditions."
exposure:
- asset_type:
    description: Bridge infrastructure inventory with point locations and structural
      identification for bridges exceeding 180 feet in length
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
license: CC-BY-4.0
lineage:
  description: Bridge infrastructure data was compiled from tabular records in GAD
    2019 township profiles and supplemented with locally-identified bridges. Geographic
    coordinates for over 980 bridges were derived and verified using high-resolution
    satellite imagery to create a point-based spatial inventory of critical transportation
    infrastructure.
  sources:
  - id: source_1
    license: null
    name: GAD 2019 township profiles
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Local knowledge
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: High resolution satellite imagery
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mimu-geonode-bridges-180ft-in-myanmar
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
- access_url: https://geonode.themimu.info/geoserver/geonode/ows?format_options=charset%3AUTF-8&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature&typename=geonode:mm_bridges_pt
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile. Point location dataset of larger bridges (>180ft)
    in Myanmar. Co-produced by CDE & MIMU based on tabular data in GAD 2019 township
    profiles and local knowledge using mostly large scale satellite imagery to identify
    geographic location.
  download_url: null
  format: null
  id: resource_40e82f6a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Bridges (>180ft) in Myanmar shapefile
- access_url: https://geonode.themimu.info/geoserver/geonode/ows?service=WFS&version=1.0.0&request=GetFeature&outputFormat=application%2Fjson&typeName=geonode:mm_bridges_pt
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. Point location dataset of larger bridges (>180ft) in
    Myanmar. Co-produced by CDE & MIMU based on tabular data in GAD 2019 township
    profiles and local knowledge using mostly large scale satellite imagery to identify
    geographic location.
  download_url: null
  format: null
  id: resource_81548209
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Bridges (>180ft) in Myanmar geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mmr_mimu_bridges180ft_20240301
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
  start: '2024-03-01'
temporal_resolution: null
title: Bridges (>180ft) in Myanmar
version: null
vulnerability: null
---
